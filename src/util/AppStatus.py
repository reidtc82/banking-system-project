from enum import Enum


class AppStatus(Enum):
    SUBMITTED = 1
    DENIED = 2
    APPROVED = 3
    CANCELLED = 4
