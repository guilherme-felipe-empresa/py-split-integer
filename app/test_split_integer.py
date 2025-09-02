from app.split_integer import split_integer
import pytest

VARS: str = "first_value,second_value,result"
TESTES_VALUES: list = [
    (8, 1, [8]),
    (6, 2, [3, 3]),
    (17, 4, [4, 4, 4, 5]),
    (32, 6, [5, 5, 5, 5, 6, 6])
]

TESTES_VALUES2: list = [
    (8, 1, [8]),
    (10, 1, [10]),
    (7, 1, [7]),
    (101, 1, [101])
]


@pytest.mark.parametrize(VARS, TESTES_VALUES)
def test_sum_of_the_parts_should_be_equal_to_value(
    first_value: int,
    second_value: int,
    result: list
) -> None:
    assert split_integer(first_value, second_value) == result


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert len(split_integer(5, 8)) == 8
    assert len(split_integer(5, 5)) == 5
    assert len(split_integer(5, 1)) == 1


@pytest.mark.parametrize(VARS, TESTES_VALUES2)
def test_should_return_part_equals_to_value_when_split_into_one_part(
    first_value: int,
    second_value: int,
    result: list
) -> None:
    assert split_integer(first_value, second_value) == result


@pytest.mark.parametrize(VARS, TESTES_VALUES)
def test_parts_should_be_sorted_when_they_are_not_equal(
    first_value: int,
    second_value: int,
    result: list
) -> None:
    assert split_integer(first_value, second_value) == result


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(1, 3) == [0, 0, 1]
