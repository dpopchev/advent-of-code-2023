import pytest
from advent2023.day1 import find_digit
from advent2023.day1 import find_calibration_value

SCENARIOS = (
    ['1abc2', '12',],
    ['pqr3stu8vwx', '38'],
    ['a1b2c3d4e5f', '15'],
    ['treb7uchet', '77']
)

@pytest.mark.parametrize('tcase, expected', SCENARIOS, ids=(s[0] for s in SCENARIOS))
def test_finding_frist_calibration_digit(tcase, expected):
    assert find_digit(tcase) == expected[0]

@pytest.mark.parametrize('tcase, expected', SCENARIOS, ids=(s[0] for s in SCENARIOS))
def test_finding_calibration_values(tcase, expected):
    assert find_calibration_value(tcase) == expected
