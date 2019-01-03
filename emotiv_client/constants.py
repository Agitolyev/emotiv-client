from enum import Enum


class SessionStatus(Enum):

    ACTIVE = "active"
    OPEN = "open"
    CLOSE = "close"


class BluetoothControlCommand(Enum):

    CONNECT = "connect"
    DISCONNECT = "disconnect"
    REFRESH = "refresh"


class StreamTypes(Enum):
    """
    Represent possible stream types described : https://emotiv.github.io/cortex-docs/#subscriptions
    """

    MOD = "mod"
    EEG = "eeg"
    COM = "com"
    FAC = "fac"
    MET = "met"
    DEV = "dev"
    POW = "pow"
    SYS = "sys"
