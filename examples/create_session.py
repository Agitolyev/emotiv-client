import asyncio

from emotiv_client.config import Config
from emotiv_client.constants import StreamTypes, SessionStatus
from emotiv_client.cortex_context import CortexContext


if __name__ == '__main__':
    context = CortexContext()

    asyncio.get_event_loop().run_until_complete(context.authorize(Config.CLIENT_ID, Config.CLIENT_SECRET, Config.LICENSE))
    auth_resp = asyncio.get_event_loop().run_until_complete(context.next())
    auth_token = auth_resp.result['_auth']

    # Create a session
    asyncio.get_event_loop().run_until_complete(context.create_session(auth_token=auth_token))
    created_session = asyncio.get_event_loop().run_until_complete(context.next())

    # Activate a session
    asyncio.get_event_loop().run_until_complete(context.create_session(auth_token=auth_token,
                                                                       status=SessionStatus.ACTIVE.value))
    session_resp = asyncio.get_event_loop().run_until_complete(context.next())
    print(session_resp.to_string(pretty=True))


