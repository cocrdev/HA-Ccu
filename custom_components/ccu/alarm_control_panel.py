import aiohttp
from homeassistant.components.alarm_control_panel import AlarmControlPanelEntity
import json
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

class CcuAlarmControlPanel(AlarmControlPanelEntity):
    """Representation of an alarm control panel."""

    def __init__(self):
        self._state = None

    @property
    def name(self):
        """Return the name of the alarm control panel."""
        return 'My Alarm Control Panel'
        
    @property
    def state(self):
        """Return the state of the alarm control panel."""
        return self._state

    async def async_update(self):
        url = "http://192.168.25.103/state/get/1"  # replace {id} with actual id
        
        timeout = aiohttp.ClientTimeout(total=10)  # defining timeout to 10 seconds
        async with aiohttp.ClientSession(timeout=timeout) as session:
            json_data = await fetch(session, url)
            json_object = json.loads(json_data)
            self._state = json_object["Partitions"][0]
    
    async def async_send_disarm_request(self):
        url = "http://192.168.25.103/state/set/1/partition"
        payload = {"state": "Disarm"}

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None

    def alarm_disarm(self, code=None):
        """Handle the alarm being disarmed."""
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.async_send_disarm_request())



async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the alarm control panel platform."""
    async_add_entities([CcuAlarmControlPanel()])