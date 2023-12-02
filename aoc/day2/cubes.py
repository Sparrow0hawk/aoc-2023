from __future__ import annotations

from dataclasses import dataclass
from itertools import batched


class CubeBag:
    def __init__(self, red: int, blue: int, green: int):
        self._red = red
        self._blue = blue
        self._green = green
        self.plays: list[Game] = []
        self._filtered_plays = None

    def add_play(self, play: str) -> None:
        self.plays.append(Game(game_line=play))

    def filter_plays(self):
        self._filtered_plays = [
            play
            for play in self.plays
            if play.check_validity(red=self._red, blue=self._blue, green=self._green)
        ]

    @property
    def valid_game_ids(self):
        return [game.id for game in self._filtered_plays]


class Game:
    def __init__(self, game_line: str):
        self._game_line = game_line
        self.id = int(self._game_line.split(":")[0].split(" ")[1])
        self.draws = [CubeDraw(**draws) for draws in self._get_draws()]

    def _get_draws(self) -> list[dict[str, str]]:
        draws = self._game_line.split(":")[1].split(";")
        draws_lists = [game.replace(",", "").strip().split(" ") for game in draws]
        return [{k: int(v) for v, k in batched(draw, 2)} for draw in draws_lists]

    def check_validity(self, red: int, blue: int, green: int) -> bool:
        return all(
            [
                draw.red <= red and draw.blue <= blue and draw.green <= green
                for draw in self.draws
            ]
        )


@dataclass
class CubeDraw:
    red: int = 0
    blue: int = 0
    green: int = 0
