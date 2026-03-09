import mathlib
import pytest
import sys

@pytest.mark.skip(reason="skipping this test. Method gonna deprecate")
# To get the reason of skipping the test: pytest -v -rxs
def test_calculate_total():
    total = mathlib.calculate_total(4,5)
    assert total == 9

# @pytest.mark.skipif(sys.version_info > (3,14), reason="skipping this test. Version mismatch")
def test_calculate_difference():
    result = mathlib.calculate_difference(10,5)
    assert result == 5

# To run test based on text selection criteria: pytest -k multiply
def test_calculate_multiply():
    result = mathlib.calculate_multiply(4,5)
    assert result == 20

# pytest -m windows
# pytest -m "not windows" -v
@pytest.mark.windows
def test_windows():
    assert True

@pytest.mark.mac
def test_mac():
    assert True