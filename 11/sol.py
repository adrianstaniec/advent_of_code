import argparse
import copy
import fileinput
import logging
import numpy as np
import sys
from typing import Callable, List

parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("-d", "--debug", action="store_true")
args = parser.parse_args()

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))
level = logging.DEBUG if args.debug else logging.INFO
logger.setLevel(level)

def read_layout():
    rows = []
    for line in fileinput.input(files=(args.input_file)):
        row = line.strip()
        rows.append(list(row))
    return rows


def print_layout(layout):
    logger.debug("")
    for row in layout:
        logger.debug("".join(row))


def n_occupied_adjacent(room: List[List[str]], y, x):
    height = len(room)
    width = len(room[0])
    n_occupied = 0
    for i in range(max(0, y - 1), min(height, y + 2)):
        for j in range(max(0, x - 1), min(width, x + 2)):
            if room[i][j] == "#" and not (i == y and j == x):
                n_occupied += 1
    return n_occupied


def in_the_room(pos, room):
    return (0 <= pos[0] and pos[0] < len(room[0])) and (
        0 <= pos[1] and pos[1] < len(room)
    )


def n_occupied_visible(room: List[List[str]], y, x):
    n_occupied = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            pos = np.array([x, y])
            vec = np.array([dx, dy])
            while True:
                pos += vec
                if not in_the_room(pos, room):
                    break
                seat = room[pos[1]][pos[0]]
                if seat == "#":
                    n_occupied += 1
                    break
                elif seat == "L":
                    break
    return n_occupied


def apply_rule1(room, count_occupied: Callable):
    """Creates a new room after applying the rule:
    "Take the seat if no neighbours"
    Doesn't modify the input.
    """
    new_room = copy.deepcopy(room)
    for i in range(len(room)):
        for j in range(len(room[i])):
            if room[i][j] == "L" and count_occupied(room, i, j) == 0:
                new_room[i][j] = "#"
    return new_room


def apply_rule2(room, count_occupied: Callable, n_sufficient_occupants):
    """Creates a new room after applying the rule:
    "Empty the seat if too many neighbours"
    Doesn't modify the input.
    """
    new_room = copy.deepcopy(room)
    for i in range(len(room)):
        for j in range(len(room[i])):
            occupied = room[i][j] == "#"
            # breakpoint()
            surrounding = count_occupied(room, i, j)
            if occupied and surrounding >= n_sufficient_occupants:
                new_room[i][j] = "L"
    return new_room


layout0 = read_layout()
print_layout(layout0)

layout = layout0
while True:
    old_layout = layout
    layout = apply_rule1(layout, n_occupied_adjacent)
    print_layout(layout)
    layout = apply_rule2(layout, n_occupied_adjacent, 4)
    print_layout(layout)
    if old_layout == layout:
        break


def count_occupied(room):
    return sum(
        1 for i in range(len(room)) for j in range(len(room[0])) if room[i][j] == "#"
    )


print("\n--- Part One ---")
print(count_occupied(layout))

print("\n--- Part Two ---")

layout = read_layout()
print_layout(layout)

old_layout = layout
while True:
    old_layout = layout
    layout = apply_rule1(layout, n_occupied_visible)
    print_layout(layout)
    layout = apply_rule2(layout, n_occupied_visible, 5)
    print_layout(layout)
    if old_layout == layout:
        break

print(count_occupied(layout))
