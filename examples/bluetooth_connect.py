import asyncio

from emotiv_client.config import Config
from emotiv_client.constants import BluetoothControlCommand
from emotiv_client.cortex_context import CortexContext


if __name__ == '__main__':
    context = CortexContext()

    asyncio.get_event_loop().run_until_complete(context.control_bluetooth_headset(BluetoothControlCommand.CONNECT,
                                                                                  Config.DEVICE_ID))
    bl_connect_resp = asyncio.get_event_loop().run_until_complete(context.next())
    print(bl_connect_resp.to_string(pretty=True))
