from enum import Enum, auto


class Direction(Enum):
    # list of directions, clockwise
    NORTH = auto()  # starts with 1
    EAST = auto()
    SOUTH = auto()
    WEST = auto()
