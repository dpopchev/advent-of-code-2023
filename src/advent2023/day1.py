from typing import Iterable
from dataclasses import dataclass

def find_digit(line: Iterable[str]) -> str:
    return next(filter(lambda _: _.isdigit(), line))

def find_calibration_value(line: str) -> str:
    return f"{find_digit(line)}{find_digit(reversed(line))}"

def find_calibration_value_sum(lines: Iterable[str]) -> int:
    return sum(map(int, (find_calibration_value(l) for l in lines)))
