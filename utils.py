from typing import List


def read_file(filepath: str) -> List[str]:
    with open(filepath, "r") as input:
        lines = input.read().splitlines()
        return lines


def sanitize_args(args: List[str]) -> List[str]:
    """Split using comma and trim whitespaces for every argument"""
    args = "".join(args).split(",")
    return [arg.strip() for arg in args if arg.strip()]
