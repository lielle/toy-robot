from enum import Enum, auto


class Direction(Enum):
    # list of directions, clockwise
    NORTH = auto()  # starts with 1
    EAST = auto()
    SOUTH = auto()
    WEST = auto()

    @staticmethod
    def first():
        return Direction(1)

    @staticmethod
    def last():
        return Direction(len(Direction))

    @property
    def left(self):
        return (
            Direction.last() if self == Direction.first() else Direction(self.value - 1)
        )

    @property
    def right(self):
        return (
            Direction.first() if self == Direction.last() else Direction(self.value + 1)
        )
