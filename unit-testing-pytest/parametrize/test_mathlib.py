from parametrize import mathlib
import pytest

@pytest.mark.parametrize("test_input, expected_output", [(5, 25), (9, 81), (10, 100)])
def test_calculate_square(test_input, expected_output):
    assert test_input * test_input == expected_output