class Position:
    def __init__(self, x: int, y: int):
        self.x = int(x)
        self.y = int(y)

    def __eq__(self, other: "Position"):
        return other.x == self.x and other.y == self.y
