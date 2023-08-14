from homeassistant import core

async def async_setup(hass: core.HomeAssistant, config: dict) -> bool:
    """Set up the Ccu component."""
    hass.helpers.discovery.load_platform('sensor', 'ccu', {}, config)
    return True
