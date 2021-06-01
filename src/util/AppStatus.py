from enum import Enum


class AppStatus(Enum):
    SUBMITTED = 1
    DENIED = 2
    PROCESSED = 3
    FUNDED = 4
