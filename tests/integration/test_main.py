from main import run_commands


def test_place_move_report():
    input = [
        "PLACE 0,0,NORTH",
        "MOVE",
        "REPORT",
    ]
    output = run_commands(input)
    assert output == ["0,1,NORTH"]


def test_place_left_report():
    input = [
        "PLACE 0,0,NORTH",
        "LEFT",
        "REPORT",
    ]
    output = run_commands(input)
    assert output == ["0,0,WEST"]


def test_place_move_move_left_move_report():
    input = [
        "PLACE 1,2,EAST",
        "MOVE",
        "MOVE",
        "LEFT",
        "MOVE",
        "REPORT",
    ]
    output = run_commands(input)
    assert output == ["3,3,NORTH"]


def test_ignore_falling_movements():
    input = [
        "PLACE 0,0,SOUTH",
        "MOVE",
        "MOVE",
        "RIGHT",
        "MOVE",
        "REPORT",
    ]
    output = run_commands(input)
    assert output == ["0,0,WEST"]


def test_place_move_report_move_report():
    input = [
        "PLACE 0,0,NORTH",
        "MOVE",
        "REPORT",
        "MOVE",
        "REPORT",
    ]
    output = run_commands(input)
    assert output == ["0,1,NORTH", "0,2,NORTH"]


def test_place_move_report_place_move_left_report():
    input = [
        "PLACE 0,0,NORTH",
        "MOVE",
        "REPORT",
        "PLACE 1,3,SOUTH",
        "MOVE",
        "LEFT",
        "REPORT",
    ]
    output = run_commands(input)
    assert output == ["0,1,NORTH", "1,2,EAST"]


def test_ignore_commands_before_place():
    input = [
        "MOVE",
        "REPORT",
        "LEFT",
        "PLACE 0,0,NORTH",
        "MOVE",
        "REPORT",
    ]
    output = run_commands(input)
    assert output == ["0,1,NORTH"]
