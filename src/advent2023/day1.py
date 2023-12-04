from typing import Iterable, Pattern
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

REVERSED_WORDED_DIGITS = { k[::-1]: v for k, v in WORDED_DIGITS.items() }

DIGIT_PATTERN = re.compile(f'[0-9]|{"|".join(WORDED_DIGITS.keys())}')
REVERSED_DIGIT_PATTERN = re.compile(f'[0-9]|{"|".join(REVERSED_WORDED_DIGITS.keys())}')

def get_first_match(line:str, pattern:Pattern) -> str:
    return next(pattern.finditer(line))[0]

def get_digit_value(digit:str, lookup:dict) -> str:
    if digit in lookup:
        return lookup[digit]
    return digit

def find_digit(line: str, is_last=False) -> str:
    if is_last:
        return get_digit_value(get_first_match(line[::-1], REVERSED_DIGIT_PATTERN), REVERSED_WORDED_DIGITS)
    return get_digit_value(get_first_match(line, DIGIT_PATTERN), WORDED_DIGITS)

def find_calibration_value(line: str) -> str:
    return f"{find_digit(line)}{find_digit(line, is_last=True)}"


def find_calibration_value_sum(lines: Iterable[str]) -> int:
    return sum(map(int, (find_calibration_value(l) for l in lines)))
