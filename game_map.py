from __future__ import annotations
from typing import Iterable, Iterator, Optional, TYPE_CHECKING

from tcod.console import Console
import numpy as np # type: ignore

from entity import Actor
import tile_types

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity


class GameMap:
    def __init__(self, engine: Engine, width: int, height: int, entities: Iterable[Entity]=()):
        self.engine = engine
        self.width, self.height = width, height
        self.entities = set(entities)

        self.tiles = np.full((width, height), fill_value=tile_types.wall, order="F")

        self.visible = np.full((width, height), fill_value=False, order="F")
        self.explored = np.full((width, height), fill_value=False, order="F")


    @property
    def actors(self) -> Iterator[Actor]:
        yield from (entity for entity in self.entities if isinstance(entity, Actor) and entity.is_alive)


    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height


    def get_blocking_entity_at_location(self, x: int, y: int) -> Optional[Entity]:
        for entity in self.entities:
            if entity.x == x and entity.y == y and entity.blocks_movement:
                return entity

        return None        


    def render(self, console: Console) -> None:
        console.tiles_rgb[0:self.width, 0:self.height] = np.select(
            condlist=[self.visible, self.explored],
            choicelist=[self.tiles["light"], self.tiles["dark"]],
            default=tile_types.SHROUD
        ) 

        for entity in self.entities:
            if self.visible[entity.x, entity.y]:
                console.print(entity.x, entity.y, entity.char, fg=entity.color)

    
    def get_actor_at_location(self, x: int, y: int) -> Optional[Actor]:
        for actor in self.actors:
            if actor.x == x and actor.y == y:
                return actor

        return None