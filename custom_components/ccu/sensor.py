import aiohttp
from homeassistant.helpers.entity import Entity
import json

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

class CcuSensor(Entity):
    """Representation of a sensor."""

    def __init__(self):
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'My Sensor'
        
    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    async def async_update(self):
        url = "http://192.168.25.103/state/get/1"  # replace {id} with actual id
        
        timeout = aiohttp.ClientTimeout(total=10)  # defining timeout to 10 seconds
        async with aiohttp.ClientSession(timeout=timeout) as session:
            json_data = await fetch(session, url)
            json_object = json.loads(json_data)
            self._state = json_object["Partitions"][0]
