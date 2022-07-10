import pytest

from models.position import Position
from models.table import Table


def test_table_0_rows_raise_value_error():
    with pytest.raises(ValueError):
        Table(0, 1)


def test_table_0_columns_raise_value_error():
    with pytest.raises(ValueError):
        Table(1, 0)


def test_is_safe_within_table():
    table = Table(5, 5)
    position = Position(1, 1)
    assert table.is_safe(position)


def test_table_is_not_safe_negative_x():
    table = Table(5, 5)
    position = Position(-1, 0)
    assert not table.is_safe(position)


def test_table_is_not_safe_negative_y():
    table = Table(5, 5)
    position = Position(0, -1)
    assert not table.is_safe(position)


def test_table_is_not_safe_outside_x():
    table = Table(8, 5)
    position = Position(5, 0)
    assert not table.is_safe(position)


def test_table_is_not_safe_outside_y():
    table = Table(5, 8)
    position = Position(0, 5)
    assert not table.is_safe(position)
