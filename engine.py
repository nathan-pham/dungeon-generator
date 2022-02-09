from tcod.console import Console
from tcod.context import Context
from tcod.map import compute_fov

from input_handlers import EventHandler

from entity import Actor

from game_map import GameMap

class Engine:
    game_map: GameMap

    def __init__(self, player: Actor):
        self.event_handler = EventHandler(self)
        self.player = player


    def handle_enemy_turns(self) -> None:
        for entity in set(self.game_map.actors) - {self.player}:
            if entity.ai:
                entity.ai.perform()


    def update_fov(self) -> None:
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius = 8
        )

        self.game_map.explored |= self.game_map.visible


    def render(self, console: Console, ctx: Context) -> None:
        self.game_map.render(console)

        ctx.present(console)
        console.clear()