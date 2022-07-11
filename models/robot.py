from copy import copy
from typing import Optional

from constants.direction import Direction
from models.position import Position


class Robot:
    def __init__(self):
        self._position: Position = None
        self._direction: Direction = None

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if not isinstance(value, Position):
            raise ValueError(f"{value} is not an instance of Position")
        self._position = value

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value: Direction):
        if not isinstance(value, Direction):
            raise ValueError(f"{value} is not an instance of Direction enum")
        self._direction = value

    @property
    def is_placed(self) -> bool:
        return self.position and self.direction

    @property
    def next_move(self) -> Optional[Position]:
        if self.is_placed:
            position = copy(self._position)
            match self._direction:
                case Direction.NORTH:
                    position.y += 1
                case Direction.EAST:
                    position.x += 1
                case Direction.SOUTH:
                    position.y -= 1
                case Direction.WEST:
                    position.x -= 1
            return position

    def place(self, position: Position, direction: Direction):
        self.position = position
        self.direction = direction

    def rotate_left(self):
        if self.is_placed:
            self._direction = self._direction.left

    def rotate_right(self):
        if self.is_placed:
            self._direction = self._direction.right

    def move(self):
        if self.is_placed:
            self._position = self.next_move

    def report(self) -> Optional[str]:
        if not self.is_placed:
            return None
        return f"{self._position.x},{self._position.y},{self._direction.name}"
