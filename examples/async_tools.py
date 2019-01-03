import asyncio


def run_synchronously(async_func):
    return asyncio.get_event_loop().run_until_complete(async_func)
