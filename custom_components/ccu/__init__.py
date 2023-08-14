# __init__.py

from homeassistant import core

async def async_setup(hass: core.HomeAssistant, config: dict) -> bool:
    """Set up the Ccu component."""
    # hass.helpers.discovery.load_platform('sensor', 'ccu', {}, config)
    hass.helpers.discovery.load_platform('alarm_control_panel', 'ccu', {}, config)
    return True
