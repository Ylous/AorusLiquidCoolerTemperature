from enum import Enum


class CoolingType(Enum):
    FANS = 1
    PUMP = 2


class CoolingMode(Enum):
    ZERO = 7
    BALANCE = 0
    PERFORMANCE = 5
    QUIET = 6
    MAX = 4
    DEFAULT = 2
    CUSTOM = 1
