from enum import Enum, auto


class Command(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    PLACE = auto()
    MOVE = auto()
    LEFT = auto()
    RIGHT = auto()
    REPORT = auto()

    @staticmethod
    def values():
        return [cmd.value for cmd in Command]
