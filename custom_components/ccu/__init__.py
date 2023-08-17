# __init__.py
from homeassistant import core, config_entries
from .const import DOMAIN

async def async_setup(hass: core.HomeAssistant, config: dict) -> bool:
    """Set up the Ccu component."""
    hass.data.setdefault(DOMAIN, {})
    return True

async def async_setup_entry(hass: core.HomeAssistant, entry: config_entries.ConfigEntry):
    """Set up CCU from a config entry."""
    hass.helpers.discovery.load_platform('alarm_control_panel', 'ccu', entry.data, {})
    return True
