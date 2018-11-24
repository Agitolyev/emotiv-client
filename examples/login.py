import asyncio
import logging

from emotiv_client.config import Config
from emotiv_client.dto import Response
from emotiv_client.cortex_context import CortexContext

log = logging.getLogger(__name__)

if __name__ == '__main__':
    log.setLevel('INFO')

    context = CortexContext()

    asyncio.get_event_loop().run_until_complete(context.login(Config.USERNAME,
                                                              Config.PASSWORD,
                                                              Config.CLIENT_ID,
                                                              Config.CLIENT_SECRET))

    login_resp = Response.of_json(asyncio.get_event_loop().run_until_complete(context.next()))
    print(login_resp.to_string(pretty=True))
