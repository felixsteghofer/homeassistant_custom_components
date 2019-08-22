import asyncio
import logging
import voluptuous as vol
import homeassistant.loader as loader
import homeassistant.helpers.config_validation as cv

from homeassistant.const import (CONF_NAME, CONF_WHITELIST, CONF_BLACKLIST)
from homeassistant.components.camera import PLATFORM_SCHEMA
from homeassistant.components.mjpeg.camera import (CONF_MJPEG_URL, CONF_STILL_IMAGE_URL, MjpegCamera)

_LOGGER = logging.getLogger(__name__)

DEPENDENCIES = ['shinobi']
DOMAIN = 'shinobi'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_WHITELIST, default=[]): cv.ensure_list,
    vol.Optional(CONF_BLACKLIST, default=[]): cv.ensure_list
})

shinobi = None


@asyncio.coroutine
def async_setup_platform(hass, config, async_add_devices, discovery_info=None):
    global shinobi
    shinobi = hass.components.shinobi

    all_monitors = shinobi.get_all_started_monitors()

    if not all_monitors:
        _LOGGER.warning('No active monitors found')
        return

    filtered_monitors = []

    whitelist = config.get(CONF_WHITELIST)
    blacklist = config.get(CONF_BLACKLIST)

    if len(whitelist) > 0:
        _LOGGER.debug('Applying whitelist: ' + str(whitelist))
        filtered_monitors = [m for m in all_monitors if m['name'] in whitelist]
    elif len(blacklist) > 0:
        _LOGGER.debug('Applying blacklist: ' + str(blacklist))
        filtered_monitors = [m for m in all_monitors if m['name'] not in blacklist]
    else:
        _LOGGER.debug('No white- or blacklist applied')
        filtered_monitors = all_monitors
    
    cameras = []    

    _LOGGER.debug('Filtered monitors: {}'.format(str([monitor['name'] for monitor in filtered_monitors])))

    for monitor in filtered_monitors:
        device_info = {
            CONF_NAME: monitor['name'],
            CONF_MJPEG_URL: shinobi.monitor_stream_url(monitor['mid']),
            CONF_STILL_IMAGE_URL: shinobi.monitor_still_url(monitor['mid'])
        }
        cameras.append(ShinobiCamera(hass, shinobi, device_info, monitor))

    if not cameras:
        _LOGGER.warning('No active cameras found')
        return

    async_add_devices(cameras)


class ShinobiCamera(MjpegCamera):
    """Representation of a Shinobi Monitor Stream."""

    def __init__(self, hass, shinobi, device_info, monitor):
        """Initialize as a subclass of MjpegCamera."""
        super().__init__(device_info)
        self.shinobi = shinobi
        self._monitor_id = monitor['mid']
        self._is_recording = None

    @property
    def should_poll(self):
        """Update the recording state periodically."""
        return True

    def update(self):
        """Update our recording state from the Shinobi API."""
        _LOGGER.debug('Updating camera state for monitor {}'.format(self._monitor_id))

        status_response = self.shinobi.get_monitor_state(self._monitor_id)

        if not status_response:
            _LOGGER.warning('Could not get status for monitor {}'.format(self._monitor_id))
            return
        _LOGGER.debug('Monitor {} is in status {}'.format(self._monitor_id, status_response['mode']))
        self._is_recording = status_response.get('status') == self.shinobi.SHINOBI_CAM_STATE['RECORDING']

    @property
    def is_recording(self):
        """Return whether the monitor is in recording mode."""
        return self._is_recording
    
