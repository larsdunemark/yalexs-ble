__version__ = "0.0.1"

from dataclasses import dataclass
from enum import Enum

COMMAND_SERVICE_UUID = "0000fe24-0000-1000-8000-00805f9b34fb"
WRITE_CHARACTERISTIC = "bd4ac611-0b45-11e3-8ffd-0800200c9a66"
READ_CHARACTERISTIC = "bd4ac612-0b45-11e3-8ffd-0800200c9a66"
SECURE_WRITE_CHARACTERISTIC = "bd4ac613-0b45-11e3-8ffd-0800200c9a66"
SECURE_READ_CHARACTERISTIC = "bd4ac614-0b45-11e3-8ffd-0800200c9a66"


class Commands(Enum):

    UNLOCK = 0x0A
    LOCK = 0x0B


class LockStatus(Enum):

    UNKNOWN = 0x00
    UNKNOWN_01 = 0x01
    UNLOCKING = 0x02
    LOCKING = 0x03
    UNLOCKED = 0x04
    LOCKED = 0x05
    UNKNOWN_06 = 0x06


VALUE_TO_LOCK_STATUS = {status.value: status for status in LockStatus}


class DoorStatus(Enum):

    UNKNOWN = 0x00
    CLOSED = 0x01
    UNKNOWN_02 = 0x02
    OPENED = 0x03
    UNKNOWN_04 = 0x04


VALUE_TO_DOOR_STATUS = {status.value: status for status in DoorStatus}


@dataclass
class LockState:

    lock: LockStatus
    door: DoorStatus
