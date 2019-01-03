import asyncio

from emotiv_client.config import Config
from emotiv_client.constants import StreamTypes, SessionStatus
from emotiv_client.cortex_context import CortexContext


if __name__ == '__main__':
    context = CortexContext()

    asyncio.get_event_loop().run_until_complete(context.authorize(Config.CLIENT_ID,
                                                                  Config.CLIENT_SECRET,
                                                                  Config.LICENSE))
    auth_resp = asyncio.get_event_loop().run_until_complete(context.next())
    auth_token = auth_resp.result['_auth']

    # Get a session
    asyncio.get_event_loop().run_until_complete(context.get_sessions(auth_token))
    session_resp = asyncio.get_event_loop().run_until_complete(context.next())
    session_id = session_resp.result[0]['id']

    asyncio.get_event_loop().run_until_complete(context.update_session(auth_token=auth_token,
                                                                       status=SessionStatus.ACTIVE,
                                                                       session=session_id))
    asyncio.get_event_loop().run_until_complete(context.next())



