import pytest

from constants.direction import Direction
from models.position import Position
from models.robot import Robot


@pytest.fixture
def setup_robot() -> Robot:
    robot = Robot()
    return robot


def test_robot_valid_place(setup_robot: Robot):
    setup_robot.place(position=Position(0, 0), direction=Direction.NORTH)


def test_robot_is_placed(setup_robot: Robot):
    setup_robot.place(position=Position(0, 0), direction=Direction.NORTH)
    assert setup_robot.is_placed


def test_robot_is_not_placed(setup_robot: Robot):
    assert not setup_robot.is_placed


def test_robot_invalid_place_position(setup_robot: Robot):
    with pytest.raises(ValueError):
        setup_robot.place(position=0, direction=Direction.NORTH)


def test_robot_invalid_place_direction(setup_robot: Robot):
    with pytest.raises(ValueError):
        setup_robot.place(position=Position(0, 0), direction="INVALID_DIRECTION")


def test_robot_left_of_north_is_west(setup_robot: Robot):
    setup_robot.place(position=Position(0, 0), direction=Direction.NORTH)
    setup_robot.rotate_left()
    assert setup_robot.direction == Direction.WEST


def test_robot_right_of_west_is_north(setup_robot: Robot):
    setup_robot.place(position=Position(0, 0), direction=Direction.WEST)
    setup_robot.rotate_right()
    assert setup_robot.direction == Direction.NORTH


def test_robot_report(setup_robot: Robot):
    setup_robot.place(position=Position(0, 0), direction=Direction.NORTH)
    assert setup_robot.report() == "0,0,NORTH"


def test_robot_next_move_north(setup_robot: Robot):
    setup_robot.place(position=Position(0, 0), direction=Direction.NORTH)
    assert setup_robot.next_move == Position(0, 1)


def test_robot_move_north(setup_robot: Robot):
    setup_robot.place(position=Position(0, 0), direction=Direction.NORTH)
    setup_robot.move()
    assert setup_robot.report() == "0,1,NORTH"


def test_robot_move_east(setup_robot: Robot):
    setup_robot.place(position=Position(0, 0), direction=Direction.EAST)
    setup_robot.move()
    assert setup_robot.report() == "1,0,EAST"


def test_robot_move_south(setup_robot: Robot):
    setup_robot.place(position=Position(0, 1), direction=Direction.SOUTH)
    setup_robot.move()
    assert setup_robot.report() == "0,0,SOUTH"


def test_robot_move_west(setup_robot: Robot):
    setup_robot.place(position=Position(1, 0), direction=Direction.WEST)
    setup_robot.move()
    assert setup_robot.report() == "0,0,WEST"
