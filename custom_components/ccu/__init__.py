from homeassistant import core


async def async_setup(hass: core.HomeAssistant, config: dict) -> bool:
    """Set up the Ccu component."""
    hass.states.async_set("ccu.world", "Hello, World!")
    return True
