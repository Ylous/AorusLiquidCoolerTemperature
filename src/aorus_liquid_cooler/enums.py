from enum import Enum


class CoolingType(int, Enum):
    FANS = 1
    PUMP = 2


class CoolingMode(int, Enum):
    ZERO = 7
    BALANCE = 0
    PERFORMANCE = 5
    QUIET = 6
    MAX = 4
    DEFAULT = 2
    CUSTOM = 1
