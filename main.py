from typing import List

from constants.command import Command
from constants.direction import Direction
from models.position import Position
from models.robot import Robot
from models.table import Table
from utils import read_file, sanitize_args
from validations import validate_input


def run_commands(command_lines: List[str]) -> List[str]:
    robot: Robot = Robot()
    table: Table = Table(rows=5, columns=5)
    output: List[str] = []

    for line in command_lines:
        command, *args = line.split(" ")
        command = Command(command)
        args = sanitize_args(args)
        match command:
            case Command.PLACE:
                x, y, direction = args
                position = Position(x, y)
                if table.is_safe(position):
                    direction = Direction[direction]
                    robot.place(position, direction)

            case Command.MOVE:
                if table.is_safe(robot.next_move):
                    robot.move()

            case Command.LEFT:
                robot.rotate_left()

            case Command.RIGHT:
                robot.rotate_right()

            case Command.REPORT:
                report = robot.report()
                if report:
                    output.append(report)
    return output


if __name__ == "__main__":
    INPUT_FILE = "input.txt"
    command_lines = read_file(INPUT_FILE)
    errors = validate_input(command_lines)

    if errors:
        print("ERRORS:")
        print(*errors, sep="\n")
    else:
        output = run_commands(command_lines)
        print(*output, sep="\n")
