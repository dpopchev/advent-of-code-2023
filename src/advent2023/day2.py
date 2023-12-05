from typing import Iterable, Mapping, Optional
from dataclasses import dataclass
import re

Line = str

@dataclass
class Game:
    id: Optional[int] = None
    is_possible: Optional[bool] = None


def make_game(line: str, limits: Mapping[str,int]) -> Game:
    return Game()


def calc_possible_games(games: Iterable[Line], limits: Mapping[str,int]) -> Optional[int]:
    return None
