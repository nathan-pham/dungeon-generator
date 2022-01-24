from typing import Tuple
import numpy as np # type: ignore

# tile graphics struct
graphic_dt = np.dtype([
    ("ch", np.int32),
    ("fg", "3B"),
    ("bg", "3B")
])

# tile struct
tile_dt = np.dtype([
    ("walkable", np.bool8),
    ("transparent", np.bool8),
    ("dark", graphic_dt)
])

def new_tile(walkable: bool, transparent: bool, dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]]):
    return np.array((walkable, transparent, dark), dtype=tile_dt)

floor = new_tile(walkable=True, transparent=True, dark=(ord(' '), (255, 255, 255), (50, 50, 150)))
wall = new_tile(walkable=False, transparent=False, dark=(ord(' '), (255, 255, 255), (0, 0, 100)))