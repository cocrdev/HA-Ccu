import aiohttp
from homeassistant.helpers.entity import Entity
from homeassistant.const import CONF_HOST
import json

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

class CcuSensor(Entity):
    """Representation of a sensor."""

    def __init__(self, host):
        self._state = None
        self._host = host

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Ccu'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    async def async_update(self):
        url = f"http://{self._host}/state/get/1"  # replace {id} with actual id

        timeout = aiohttp.ClientTimeout(total=10)  # defining timeout to 10 seconds
        async with aiohttp.ClientSession(timeout=timeout) as session:
            json_data = await fetch(session, url)
            json_object = json.loads(json_data)
            self._state = json_object["Partitions"][0]

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the sensor platform."""
    async_add_entities([CcuSensor(CONF_HOST)])
