import json
import ssl
import asyncio

import websockets
from emotiv_client.config import Config
from emotiv_client.dto import Request, Response
from emotiv_client.constants import SessionStatus, BluetoothControlCommand


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

    async def get_license_info(self, auth_token):
        method = "getLicenseInfo"
        params = {
            "_auth": auth_token
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

    async def create_session(self, auth_token, **kwargs):
        """
        Creates a new session with status "open"
        :param auth_token: authentication token
        :param kwargs                       optional session update request parameters :
               headset          : (string)  Headset ID link with session (if not set Cortex will link with first headset connected)
               project          : (string)  Project name for session
               title            : (string)  Title name for session
               subject          : (string)  Reserved for future use
               experimentID     : (number)  specific experiment id for the application

        Detailed description may be found here - https://emotiv.github.io/cortex-docs/#updatesession
        """

        method = "createSession"
        params = {
            "_auth": auth_token,
            "status": SessionStatus.OPEN.value
        }
        # Merge required params with optional ones
        params = {**params, **kwargs}

        request = Request.of(method, params)
        await self._websocket.send(request.to_string())

    async def update_session(self, auth_token, status: SessionStatus, **kwargs):
        """
        Updates an existing session
        :param auth_token       : (string)           authentication token
        :param status           : (string)           New session status ("open", "close", "active")
        :param kwargs                                optional session update request parameters :
               session          : (string)           session id. If this param not set, Cortex will get first session in session list do not close
               recordingName    : (string)
               recordingNote    : (string)
               recordingSubject : (string)
               tags             : (array of strings)

        Detailed description may be found here - https://emotiv.github.io/cortex-docs/#updatesession
        """

        method = "updateSession"
        params = {
            "_auth": auth_token,
            "status": status.value
        }
        request = Request.of(method, params)
        await self._websocket.send(request.to_string())

    async def get_sessions(self, auth_token):
        method = "querySessions"
        params = {
            "_auth": auth_token
        }
        request = Request.of(method, params)
        await self._websocket.send(request.to_string())

    async def subscribe(self, auth_token, session_id, data_streams: list):
        method = "subscribe"
        params = {
            "_auth": auth_token,
            "session": session_id,
            "streams": [channel.value for channel in data_streams]
        }
        request = Request.of(method, params)
        await self._websocket.send(request.to_string())

    async def next(self) -> Response:
        return Response.of_json(json.loads(await self._websocket.recv()))
