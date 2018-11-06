import ssl
import json
import asyncio
import websockets

from emotiv_client.config import Config
from emotiv_client.dto import Request

ssl_context = ssl._create_unverified_context()


async def hello(uri, request):

    async with websockets.connect(uri, ssl=ssl_context) as websocket:
        await websocket.send(request)

        async for message in websocket:
            print(message)

if __name__ == '__main__':
    method = "queryHeadsets"
    params = {}
    request = Request(method, params, 1)

    asyncio.get_event_loop().run_until_complete(
        hello(Config.URL, json.dumps(request.__dict__)))
