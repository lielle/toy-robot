from validations import validate_input


def test_invalid_command():
    input = [
        "PLACE 0,0,NORTH",
        "INVALID",
    ]
    errors = validate_input(input)
    assert "Invalid command" in "\n".join(errors)


def test_command_doesnt_accept_args():
    input = [
        "PLACE 0,0,NORTH",
        "REPORT this_shouldnt_be_here",
    ]
    errors = validate_input(input)
    assert "doesn't accept arguments" in "\n".join(errors)


def test_insufficient_place_args():
    input = [
        "PLACE 0,0",
    ]
    errors = validate_input(input)
    assert "PLACE command should have 3 args" in "\n".join(errors)


def test_excessive_place_args():
    input = [
        "PLACE 0,0,SOUTH,oops",
    ]
    errors = validate_input(input)
    assert "PLACE command should have 3 args" in "\n".join(errors)


def test_invalid_x():
    input = [
        "PLACE not_int,0,SOUTH",
    ]
    errors = validate_input(input)
    assert "x should be an int" in "\n".join(errors)


def test_invalid_y():
    input = [
        "PLACE 0,not_int,SOUTH",
    ]
    errors = validate_input(input)
    assert "y should be an int" in "\n".join(errors)


def test_invalid_direction():
    input = [
        "PLACE 0,0,INVALID",
    ]
    errors = validate_input(input)
    assert "Not in accepted direction values" in "\n".join(errors)
