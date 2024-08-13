import enum
from collections.abc import Iterable
from dataclasses import InitVar, dataclass, field


class GameOutcome(enum.Enum):
    POSSIBLE = enum.auto()
    IMPOSSIBLE = enum.auto()

    def __str__(self) -> str:
        return self.name.lower()


@dataclass
class Game:
    red: int
    green: int
    blue: int


@dataclass
class GameRecord:
    id: int
    games: InitVar[Iterable[Game]]
    _games: list[Game] = field(init=False, default_factory=list)

    def __post_init__(self, games: Iterable[Game]) -> None:
        self._games = [g for g in games]

    def append(self, game: Game) -> None:
        self._games.append(game)


def make_game_record(record: str) -> GameRecord:
    return GameRecord(-10, [Game(-10, -10, -10)])
