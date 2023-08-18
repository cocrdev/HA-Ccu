# __init__.py
from homeassistant import core, config_entries
from .const import DOMAIN

async def async_setup(hass: core.HomeAssistant, config: dict) -> bool:
    """Set up the Ccu component."""
    hass.data.setdefault(DOMAIN, {})
    return True

async def async_setup_entry(hass: core.HomeAssistant, entry: config_entries.ConfigEntry):
    """Set up CCU from a config entry."""
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(
            entry, "alarm_control_panel"
        )
    )
    return True
