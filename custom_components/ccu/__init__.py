# __init__.py

from homeassistant import core, config_entries


async def async_setup(hass: core.HomeAssistant, config: dict) -> bool:
    """Set up the Ccu component."""
    # hass.helpers.discovery.load_platform('sensor', 'ccu', {}, config)
    hass.helpers.discovery.load_platform('alarm_control_panel', 'ccu', {}, config)
    return True

async def async_setup_entry(hass: core.HomeAssistant, entry: config_entries.ConfigEntry):
    """Set up CCU from a config entry."""
    # TODO: Set up your integration based on the config entry data
    return True
