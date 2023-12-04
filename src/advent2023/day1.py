from typing import Iterable, Optional
def find_digit(line: Iterable[str]) -> Optional[str]:
    return next(filter(lambda _: _.isdigit(), line), None)


def find_calibration_value(line: str) -> Optional[str]:
    return f"{find_digit(line)}{find_digit(reversed(line))}"
