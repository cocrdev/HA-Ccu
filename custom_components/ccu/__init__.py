from homeassistant import core
from homeassistant.helpers.entity_platform import async_add_entities
from sensor import CcuSensor

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the sensor platform."""
    async_add_entities([CcuSensor()])


async def async_setup(hass: core.HomeAssistant, config: dict) -> bool:
    """Set up the Ccu component."""
    hass.states.async_set("ccu.world", "Hello, World!")
    return True
