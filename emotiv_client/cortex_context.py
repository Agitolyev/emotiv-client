import json
import ssl
import asyncio

import websockets
from emotiv_client.config import Config
from emotiv_client.dto import Request, Response
from emotiv_client.constant import SessionStartStatus, BluetoothControlCommand


class CortexContext(object):

    def __init__(self, url: str = Config.URL, ssl_context=ssl._create_unverified_context()):
        self._url = url
        self._ssl_context = ssl_context
        self._websocket = asyncio.get_event_loop()\
            .run_until_complete(websockets.connect(self._url, ssl=self._ssl_context))

    async def get_devices(self):
        method = "queryHeadsets"
        params = {}
        request = Request.of(method, params)
        await self._websocket.send(request.to_string())

    async def login(self, uname, password, client_id, client_secret):
        method = "login"
        params = {
            "username": uname,
            "password": password,
            "client_id": client_id,
            "client_secret": client_secret
        }
        request = Request.of(method, params)
        await self._websocket.send(request.to_string())

    async def authorize(self, client_id, client_secret, license, debit=0):
        method = "authorize"
        params = {
            "client_id": client_id,
            "client_secret": client_secret,
            "license": license,
            "debit": debit
        }
        request = Request.of(method, params)
        await self._websocket.send(request.to_string())

    async def generate_new_token(self, token):
        method = "generateNewToken"
        params = {
            "token": token
        }
        request = Request.of(method, params)
        await self._websocket.send(request.to_string())

    async def get_license_info(self, token):
        method = "getLicenseInfo"
        params = {
            "_auth": token
        }
        request = Request.of(method, params)
        await self._websocket.send(request.to_string())

    async def control_bluetooth_headset(self, command: BluetoothControlCommand,  headset_id=None):
        method = "controlBluetoothHeadset"
        params = {
            "command": command.value,
            "headset": headset_id
        }
        request = Request.of(method, params)
        await self._websocket.send(request.to_string())

    async def create_emotiv_session(self, token, status: SessionStartStatus, project=None, title=None, subject=None):
        method = "createSession"
        params = {
            "_auth": token,
            "status": status.value,
            "project": project,
            "title": title,
            "subject": subject
        }
        request = Request.of(method, params)
        await self._websocket.send(request.to_string())

    async def next(self) -> Response:
        return Response.of_json(json.loads(await self._websocket.recv()))
