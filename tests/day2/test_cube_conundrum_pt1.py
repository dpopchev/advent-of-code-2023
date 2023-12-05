from types import MappingProxyType
import pytest
from advent2023.day2 import calc_possible_games
from advent2023.day2 import make_game

SCENARIO_LIMITS = MappingProxyType( {'red': 12,
                                     'green': 13,
                                     'blue': 14
                                     } )

SCENARIO_GAMES = (
    ('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', True),
    ('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue', True),
    ('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red', False),
    ('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red', False),
    ('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green', True),
)

class TestGameCreation:
    @pytest.mark.parametrize('game_id, game', ((i, g) for i, g in enumerate(SCENARIO_GAMES,1)),ids=range(1, len(SCENARIO_GAMES)+1))
    def test_game_id_field(self, game_id, game):
        assert make_game(game, SCENARIO_LIMITS).id == game_id

    @pytest.mark.parametrize('game, expected', SCENARIO_GAMES,ids=range(1, len(SCENARIO_GAMES)+1))
    def test_game_is_possible_field(self, game, expected):
        assert make_game(game, SCENARIO_LIMITS).is_possible == expected


def test_sum_possible_games_ids():
    assert calc_possible_games(SCENARIO_GAMES, SCENARIO_LIMITS) == 8
