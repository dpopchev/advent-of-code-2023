from collections.abc import Sequence
from dataclasses import dataclass

import pytest

from advent2023.day2 import Game, GameOutcome


@dataclass
class RecordedGame:
    record: str
    outcome: GameOutcome


RECORDED_GAMES: Sequence[RecordedGame] = (
    RecordedGame(
        'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
        GameOutcome.POSSIBLE),
    RecordedGame(
        'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
        GameOutcome.POSSIBLE),
    RecordedGame(
        'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
        GameOutcome.IMPOSSIBLE),
    RecordedGame(
        'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
        GameOutcome.IMPOSSIBLE),
    RecordedGame('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
                 GameOutcome.POSSIBLE)
)
GAME_LIMITATIONS: Game = Game(12, 13, 14)


@pytest.fixture
def game1() -> RecordedGame:
    return RECORDED_GAMES[0]
