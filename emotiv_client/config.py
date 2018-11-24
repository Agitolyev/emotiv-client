import os


class Config(object):
    URL = "wss://emotivcortex.com:54321"
    USERNAME = os.getenv('EMOTIV_USERNAME', None)
    PASSWORD = os.getenv('EMOTIV_PASSWORD', None)
    CLIENT_ID = os.getenv('EMOTIV_CLIENT_ID', None)
    CLIENT_SECRET = os.getenv('EMOTIV_CLIENT_SECRET', None)
    # License Key
    LICENSE = os.getenv('EMOTIV_LICENSE', None)
    DEVICE_ID = os.getenv('EMOTIV_DEVICE_ID', None)
