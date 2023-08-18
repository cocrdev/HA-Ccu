from abc import ABC, abstractmethod
import aiohttp
import json
from typing import Dict, List
from .types import State


class ICcuDevice(ABC):
    @abstractmethod
    def update(self):
        raise NotImplementedError('update() not implemented')


class Ccu:
    def __init__(self, host: str) -> None:
        self._host : str = host
        self.state_device : State = {}

    async def _fetch(self, session: aiohttp.ClientSession, url: str) -> str:
        async with session.get(url) as response:
            return await response.text()

    async def _get_controllers(self) -> List[int]:
        pass

    async def _get_controller_state(self, id: int) -> Dict[str, str]:
        pass

    async def update(self):
        url : str = f"http://{self._host}/state/get/1"  # replace {id} with actual id
        json_object : Dict = dict()
        state : State = dict()

        timeout : ClientTimeout = aiohttp.ClientTimeout(total=10)  # defining timeout to 10 seconds
        async with aiohttp.ClientSession(timeout=timeout) as session:
            response_data : str = await self._fetch(session, url)
            json_object = json.loads(response_data)
            state = {"state": json_object["Partitions"][0]}

        self.state_device = state
        return state
