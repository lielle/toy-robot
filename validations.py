from typing import List

from constants.command import Command
from constants.direction import Direction
from utils import sanitize_args


def validate_input(command_lines: List[str]) -> List[str]:
    errors = []
    for line in command_lines:
        command, *args = line.split(" ")
        args = sanitize_args(args)

        if command == Command.PLACE.value:
            errors.extend(get_place_args_errors(args))
        elif command in Command._member_names_:
            if args:
                errors.append(f"{command} doesn't accept arguments. Received: {args}")
        else:
            errors.append(f"Invalid command: `{command}`")
    return errors


def get_place_args_errors(args) -> List[str]:
    errors = []
    if len(args) != 3:
        errors.append(
            "PLACE command should have 3 args separated by comma: x,y,direction"
        )
        return errors

    x, y, direction = args
    try:
        int(x)
    except:
        errors.append(f"x should be an int. Received: {x}")
    try:
        int(y)
    except:
        errors.append(f"y should be an int. Received: {y}")

    if direction not in Direction._member_names_:
        errors.append(
            f"Not in accepted direction values {Direction._member_names_}. Received: {direction}"
        )
    return errors
