from __future__ import annotations
from typing import Tuple, Optional, TYPE_CHECKING

import copy

if TYPE_CHECKING:
    from game_map import GameMap


class Entity:
    def __init__(
        self, 
        game_map: Optional[GameMap] = None,
        x: int = 0, 
        y: int = 0, 
        char: str = "?", 
        color: Tuple[int, int, int] = (255, 255, 255),
        name: str = "Untitled Entity",
        blocks_movement: bool = False
    ):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks_movement = blocks_movement

        if game_map:
            self.game_map = game_map
            game_map.entities.add(self)


    def spawn(self, game_map: GameMap, x: int, y: int) -> Entity:
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        clone.game_map = game_map

        game_map.entities.add(clone)

        return clone


    def place(self, x: int, y: int, game_map: Optional[GameMap] = None) -> None:
        self.x = x
        self.y = y

        if game_map:
            if hasattr(self, "game_map"):
                self.game_map.entities.remove(self)

            self.game_map = game_map
            self.game_map.entities.add(self)

    def move(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy