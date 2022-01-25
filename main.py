import tcod

# event listeners
from input_handlers import EventHandler
from engine import Engine

from procgen import generate_dungeon

# player
from entity import Entity

def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    tileset = tcod.tileset.load_tilesheet(
        "./tileset.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    # create entities
    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2) - 5, int(screen_height / 2), "@", (255, 255, 0))
    entities = {player, npc}

    game_map = generate_dungeon(max_rooms, room_min_size, room_max_size, map_width, map_height, player)
    engine = Engine(entities, event_handler, game_map, player)

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
            engine.handle_events(tcod.event.wait())

if __name__ == "__main__":
    main()
