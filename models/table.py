from models.position import Position


class Table:
    def __init__(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns

    @property
    def rows(self):
        return self._rows

    @rows.setter
    def rows(self, value):
        value = int(value)
        if value < 1:
            raise ValueError(f"rows cannot be less than 1: {value}")
        self._rows = value

    @property
    def columns(self):
        return self._columns

    @columns.setter
    def columns(self, value):
        value = int(value)
        if value < 1:
            raise ValueError(f"columns cannot be less than 1: {value}")
        self._columns = value

    def is_safe(self, position: Position) -> bool:
        if not position:
            return False
        is_x_safe = 0 <= position.x < self.columns
        is_y_safe = 0 <= position.y < self.rows
        return is_x_safe and is_y_safe
