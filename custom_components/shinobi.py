import asyncio
import logging
import requests
import json
import voluptuous as vol
import homeassistant.helpers.config_validation as cv

from homeassistant.const import (
    CONF_HOST, CONF_API_KEY, CONF_SSL)

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'shinobi'
DEFAULT_TIMEOUT = 10
DEFAULT_SSL = False

SHINOBI_CAM_DISABLED = 'stop'
SHINOBI_CAM_WATCHING = 'start'
SHINOBI_CAM_RECORDING = 'record'

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Required(CONF_HOST): cv.string,
        vol.Required(CONF_API_KEY): cv.string,
        vol.Required('group_key'): cv.string,
        vol.Optional(CONF_SSL, default=DEFAULT_SSL): cv.boolean,
        vol.Optional('monitors', default=[]): cv.ensure_list
    })
}, extra=vol.ALLOW_EXTRA)


@asyncio.coroutine
def async_setup(hass, config):

    global SHINOBI
    SHINOBI = {}

    conf = config[DOMAIN]
    if conf[CONF_SSL]:
        schema = 'https'
    else:
        schema = 'http'
    
    server_origin = '{}://{}'.format(schema, conf[CONF_HOST])
    
    SHINOBI['server_origin'] = server_origin
    SHINOBI['api_key'] = conf.get(CONF_API_KEY, None)
    SHINOBI['group_key'] = conf.get('group_key', None)
    SHINOBI['monitors'] = conf.get('monitors')

    hass.data[DOMAIN] = SHINOBI

    # unfortunately, the api does not return error codes. The only way to check if the credentials are working is to check the response of an (arbitrary) request (e.g. get all monitors)
    try:
        check_creds_response = get_all_started_monitors()
    except:
        return False
    
    # expected response contains a list with activated monitors (or an empty list)
    if isinstance(check_creds_response, list):
        return True
    else:
        # response payload contains ok: false if authentication has not been successful
        if not check_creds_response.ok:
            _LOGGER.error('Wrong api_key or non existing group_key provided')
        else:
            _LOGGER.error('Unknown error occured while retrieving monitors')
        
        return False


def _shinobi_request(api_path, method='get', data=None):
    """Perform a Shinobi request."""

    api_base = SHINOBI['server_origin'] + '/' + SHINOBI['api_key']

    req = requests.get(api_base + api_path, timeout=DEFAULT_TIMEOUT)

    # TODO some more error handling here?
    try:
        response = req.json()
    except ValueError:
        _LOGGER.exception('JSON decode exception caught while attempting to '
                        'decode "{}"', req.text)
    return response


def get_all_started_monitors():
    """Get all started monitors from the Shinobi API."""
    _LOGGER.debug('Sending request to Shinobi to get all started monitors')

    get_monitors_path = '/smonitor/' + SHINOBI['group_key']

    response = _shinobi_request(get_monitors_path)

    # TODO is it necessary to save monitors globally in SHINOBI?
    SHINOBI['monitors'] = response

    _LOGGER.debug('Shinobi returned {} monitors: {}'.format(str(len(SHINOBI['monitors'])), str([monitor['name'] for monitor in SHINOBI['monitors']])))

    return SHINOBI['monitors']


def get_monitor_state(monitor_id):
    """Get the state of a monitor."""
    api_path = '/monitor/{}/{}'.format(SHINOBI['group_key'], monitor_id)
    return _shinobi_request(api_path)


def set_monitor_state(monitor_id, mode):
    """Get the state of a monitor."""
    if not (mode == SHINOBI_CAM_DISABLED or mode == SHINOBI_CAM_WATCHING or mode == SHINOBI_CAM_RECORDING):
        raise ValueError('monitor state must be either {}, {} or {}'.format(SHINOBI_CAM_DISABLED, SHINOBI_CAM_WATCHING, SHINOBI_CAM_RECORDING))
    api_path = '/monitor/{}/{}'.format(SHINOBI['group_key'], monitor_id)
    return _shinobi_request(api_path)


def monitor_stream_url(monitor_id):
    """Get the stream url. See https://shinobi.video/docs/api#content-embedding-streams for more information."""
    return SHINOBI['server_origin'] + '/' + SHINOBI['api_key'] + '/mjpeg/' + SHINOBI['group_key'] + '/' + monitor_id


def monitor_still_url(monitor_id):
    """Get the url of still jpg images. Snapshots must be enabled in cam settings, see https://shinobi.video/docs/api#content-get-streams"""
    return SHINOBI['server_origin'] + '/' + SHINOBI['api_key'] + '/jpeg/' + SHINOBI['group_key'] + '/' + monitor_id + '/s.jpg'
