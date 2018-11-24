from enum import Enum


class SessionStartStatus(Enum):

    ACTIVE = "active"
    OPEN = "open"


class BluetoothControlCommand(Enum):

    CONNECT = "connect"
    DISCONNECT = "disconnect"
    REFRESH = "refresh"
