import tcod

# event listeners
from engine import Engine

from procgen import generate_dungeon
import entity_factories

from config import *

import copy

def main() -> None:
    tileset = tcod.tileset.load_tilesheet(
        "./tileset.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    player = copy.deepcopy(entity_factories.player)
    engine = Engine(player)

    engine.game_map = generate_dungeon(max_rooms, room_min_size, room_max_size, map_width, map_height, max_monsters_per_room, engine)
    engine.update_fov()

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet Another Rougelike Tutorial",
        vsync=True
    ) as ctx:
        root_console = tcod.Console(screen_width, screen_height, order="F")

        while True:
            engine.render(root_console, ctx)
            engine.event_handler.handle_events()

if __name__ == "__main__":
    main()
