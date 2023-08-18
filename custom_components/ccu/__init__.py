# __init__.py
from homeassistant import core, config_entries
from homeassistant.const import CONF_HOST, CONF_SCAN_INTERVAL
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from .const import DOMAIN
from .ccu import Ccu
from typing import Dict
import logging


_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: core.HomeAssistant, entry: config_entries.ConfigEntry):
    """Set up CCU from a config entry."""
    ccu : Ccu = Ccu(entry.data[CONF_HOST])
    coordinator : DataUpdateCoordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name=DOMAIN,
        update_method=ccu.update,
        update_interval=CONF_SCAN_INTERVAL,
    )
    await coordinator.async_config_entry_first_refresh()
    hass.data[DOMAIN] : Dict[str, str] = {
        "coordinator": coordinator,
    }
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(
            entry, "alarm_control_panel"
        )
    )
    return True
