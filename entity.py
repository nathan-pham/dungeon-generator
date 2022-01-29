from __future__ import annotations
from typing import Tuple, TypeVar, TYPE_CHECKING

import copy

if TYPE_CHECKING:
    from game_map import GameMap


class Entity:
    def __init__(
        self, 
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

    
    def spawn(self, game_map: GameMap, x: int, y: int) -> Entity:
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y

        game_map.entities.add(clone)

        return clone


    def move(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy