import asyncio
import logging
import homeassistant.loader as loader

from homeassistant.const import CONF_NAME
from homeassistant.components.camera.mjpeg import (
    CONF_MJPEG_URL, CONF_STILL_IMAGE_URL, MjpegCamera)

_LOGGER = logging.getLogger(__name__)

DEPENDENCIES = ['shinobi']
DOMAIN = 'shinobi'

shinobi = loader.get_component('shinobi')


@asyncio.coroutine
def async_setup_platform(hass, config, async_add_devices, discovery_info=None):
    monitors = shinobi.get_all_started_monitors()
    cameras = []

    _LOGGER.debug(config)
    
    if not monitors:
        _LOGGER.warning('No active monitors found')
        return

    for monitor in monitors:
        device_info = {
            CONF_NAME: monitor['name'],
            CONF_MJPEG_URL: shinobi.monitor_stream_url(monitor['mid']),
            CONF_STILL_IMAGE_URL: shinobi.monitor_still_url(monitor['mid'])
        }
        cameras.append(ShinobiCamera(hass, device_info, monitor))

    if not cameras:
        _LOGGER.warning('No active cameras found')
        return

    async_add_devices(cameras)


class ShinobiCamera(MjpegCamera):
    """Representation of a Shinobi Monitor Stream."""

    def __init__(self, hass, device_info, monitor):
        """Initialize as a subclass of MjpegCamera."""
        super().__init__(hass, device_info)
        self._monitor_id = monitor['mid']
        self._is_recording = None

    @property
    def should_poll(self):
        """Update the recording state periodically."""
        return True

    def update(self):
        """Update our recording state from the Shinobi API."""
        _LOGGER.debug('Updating camera state for monitor {}'.format(self._monitor_id))

        status_response = shinobi.get_monitor_state(self._monitor_id)

        if not status_response:
            _LOGGER.warning('Could not get status for monitor {}'.format(self._monitor_id))
            return
        _LOGGER.debug('Monitor {} is in status {}'.format(self._monitor_id, status_response['mode']))
        self._is_recording = status_response.get('status') == shinobi.SHINOBI_CAM_RECORDING

    @property
    def is_recording(self):
        """Return whether the monitor is in recording mode."""
        return self._is_recording
    