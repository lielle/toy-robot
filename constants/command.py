from enum import Enum


class Command(Enum):
    PLACE = "PLACE"
    MOVE = "MOVE"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    REPORT = "REPORT"

    @staticmethod
    def values():
        return [cmd.value for cmd in Command]
