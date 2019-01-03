import asyncio
import logging
import time

from emotiv_client.config import Config
from emotiv_client.cortex_context import CortexContext

log = logging.getLogger(__name__)

if __name__ == '__main__':
    context = CortexContext()

    asyncio.get_event_loop().run_until_complete(context.authorize(Config.CLIENT_ID,
                                                                  Config.CLIENT_SECRET,
                                                                  Config.LICENSE))
    auth_resp = asyncio.get_event_loop().run_until_complete(context.next())
    auth_token = auth_resp.result['_auth']

    while True:
        asyncio.get_event_loop().run_until_complete(context.get_sessions(auth_token))
        resp_sessions = asyncio.get_event_loop().run_until_complete(context.next())
        print(resp_sessions.to_string(pretty=True))
        time.sleep(10)

