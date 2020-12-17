"""My solution to https://adventofcode.com/2020/day/17#part2"""

import argparse
import fileinput
import logging
import sys

import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", action="store_true")
parser.add_argument("-i", "--input", default="input.txt")
args = parser.parse_args()

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.INFO)
if args.debug:
    logger.setLevel(logging.DEBUG)


#               __
#  _______  ___/ /__
# / __/ _ \/ _  / -_)
# \__/\___/\_,_/\__/
#


def parse():
    state = []
    for line in fileinput.input(files=(args.input)):
        line = line.strip()
        state.append([1 if c == "#" else 0 for c in line])
    pocket = np.array(state, dtype=np.int8)
    logger.debug(pocket)
    pocket = np.expand_dims(pocket, 0)
    return np.expand_dims(pocket, 0)


def count_active_neighbours(pocket, w, z, x, y):
    cnt = 0
    for l in range(w - 1, w + 2):
        for k in range(z - 1, z + 2):
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if l == w and k == z and i == x and j == y:
                        continue
                    if l < 0 or k < 0 or i < 0 or j < 0:
                        continue
                    if (
                        l > pocket.shape[0] - 1
                        or k > pocket.shape[1] - 1
                        or i > pocket.shape[2] - 1
                        or j > pocket.shape[3] - 1
                    ):
                        continue
                    else:
                        if pocket[l, k, i, j] == 1:
                            cnt += 1
    return cnt


def step(pocket):
    pocket = np.pad(pocket, 1)
    new_pocket = np.zeros(pocket.shape, dtype=np.int8)
    shape = pocket.shape
    for l in range(shape[0]):
        for k in range(shape[1]):
            for i in range(shape[2]):
                for j in range(shape[3]):
                    c = count_active_neighbours(pocket, l, k, i, j)
                    active = pocket[l, k, i, j] == 1
                    # If a cube is active and
                    # exactly 2 or 3 of its neighbors are also active,
                    # the cube remains active. Otherwise, the cube becomes inactive.
                    if active:
                        if 2 <= c and c <= 3:
                            new_state = 1
                        else:
                            new_state = 0
                    else:
                        # If a cube is inactive but exactly 3 of its neighbors are active,
                        # the cube becomes active. Otherwise, the cube remains inactive.
                        if c == 3:
                            new_state = 1
                        else:
                            new_state = 0
                    new_pocket[l, k, i, j] = new_state

    logger.debug(new_pocket)
    return new_pocket


def main():
    pocket = parse()
    for _ in range(6):
        pocket = step(pocket)
    print("--- Part Two ---")
    print(np.sum(pocket))


if __name__ == "__main__":
    main()
