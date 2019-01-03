import asyncio
import logging

from emotiv_client.config import Config
from emotiv_client.constants import StreamTypes
from emotiv_client.cortex_context import CortexContext

log = logging.getLogger(__name__)

if __name__ == '__main__':
    context = CortexContext()

    asyncio.get_event_loop().run_until_complete(context.authorize(Config.CLIENT_ID,
                                                                  Config.CLIENT_SECRET,
                                                                  Config.LICENSE))
    auth_resp = asyncio.get_event_loop().run_until_complete(context.next())
    auth_token = auth_resp.result['_auth']

    # Create a session
    asyncio.get_event_loop().run_until_complete(context.create_session(auth_token=auth_token))
    asyncio.get_event_loop().run_until_complete(context.next())

    # Get a session
    asyncio.get_event_loop().run_until_complete(context.get_sessions(auth_token))
    session_resp = asyncio.get_event_loop().run_until_complete(context.next())
    session_id = session_resp.result[1]['id']
    print(session_id)

    asyncio.get_event_loop().run_until_complete(context.subscribe(auth_token, session_id, [StreamTypes.EEG]))
    resp_sessions = asyncio.get_event_loop().run_until_complete(context.next())
    print(resp_sessions.to_string(pretty=True))

