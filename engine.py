

from typing import Any, Iterable, Set

from tcod.console import Console
from tcod.context import Context
from tcod.map import compute_fov

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

from entity import Entity

from game_map import GameMap

class Engine:

    def __init__(self, entities: Set[Entity], event_handler: EventHandler, game_map: GameMap, player: Entity):
        self.entities = entities
        self.event_handler = event_handler
        self.game_map = game_map
        self.player = player

        self.update_fov()

    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            action = self.event_handler.dispatch(event)

            if action is None: continue
            action.perform(self, self.player)
            
            self.update_fov()

    def update_fov(self) -> None:
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius = 8
        )

        self.game_map.explored |= self.game_map.visible

    def render(self, console: Console, ctx: Context) -> None:
        self.game_map.render(console)

        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, fg=entity.color)

        ctx.present(console)
        console.clear()
            