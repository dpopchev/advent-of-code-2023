from typing import Iterable
import re

WORDED_DIGITS = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

DIGIT_PATTERN = re.compile(f'[0-9]|{"|".join(WORDED_DIGITS.keys())}')

def find_digit(line: str, is_last=False) -> str:
    matches = (m[0] for m in DIGIT_PATTERN.finditer(line))
    digits = [WORDED_DIGITS[m] if m in WORDED_DIGITS else m for m in matches]
    if is_last:
        return digits[-1]
    return digits[0]

def find_calibration_value(line: str) -> str:
    return f"{find_digit(line)}{find_digit(line, is_last=True)}"


def find_calibration_value_sum(lines: Iterable[str]) -> int:
    return sum(map(int, (find_calibration_value(l) for l in lines)))
