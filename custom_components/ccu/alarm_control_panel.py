# alarm_control_panel.py
import aiohttp
from homeassistant.components.alarm_control_panel import AlarmControlPanelEntity
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
    UpdateFailed,
)
from homeassistant.const import CONF_HOST
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import callback
import json
import logging
from .const import DOMAIN


_LOGGER = logging.getLogger(__name__)

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

class CcuAlarmControlPanel(AlarmControlPanelEntity, CoordinatorEntity):
    """Representation of an alarm control panel."""

    def __init__(self, host: str, coordinator: DataUpdateCoordinator):
        super().__init__(coordinator)
        self._state : str = None
        self._host : str = host

    @property
    def name(self):
        """Return the name of the alarm control panel."""
        return 'Ccu state'

    @property
    def state(self):
        """Return the state of the alarm control panel."""
        return self._state
    
    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self._state = self.coordinator.data['state']
        self.async_write_ha_state()

    async def async_update(self):
        self._state = self.coordinator.data['state']

    async def async_send_disarm_request(self):
        url = f"http://{self._host}/state/set/1/partition"
        payload = {"state": "Disarm"}

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None

    async def async_alarm_disarm(self, code=None) -> None:
        """Send disarm command."""
        await self.async_send_disarm_request()
        await self.coordinator.async_request_refresh()


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    host : str = config.data[CONF_HOST]
    coordinator : DataUpdateCoordinator = hass.data[DOMAIN]["coordinator"]
    """Set up the alarm control panel from a config entry."""
    async_add_entities([CcuAlarmControlPanel(host, coordinator)])

async def async_setup_entry(hass, config_entry: ConfigEntry, async_add_devices):
    host : str = config_entry.data[CONF_HOST]
    coordinator : DataUpdateCoordinator = hass.data[DOMAIN]["coordinator"]
    """Set up the alarm control panel from a config entry."""
    async_add_devices([CcuAlarmControlPanel(host, coordinator)])
