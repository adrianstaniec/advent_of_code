"""My solution to https://adventofcode.com/2020/day/12"""

import argparse
import logging
import fileinput
import sys
from math import sin, cos
import numpy as np

#    __       __
#   / /  ___ / /__  ___ ____
#  / _ \/ -_) / _ \/ -_) __/
# /_//_/\__/_/ .__/\__/_/
#           /_/

parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.add_argument("-d", "--debug", action="store_true")
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


def rotate_vector(vec, deg):
    vec = np.array(vec)
    rad = deg / 180 * np.pi
    R = np.array([[cos(rad), -sin(rad)], [sin(rad), cos(rad)]])
    assert abs(deg) in [90, 180, 270, 360]
    return np.round((R @ vec)).astype(int)


def main():
    print("--- Part One ---")
    pos = np.array([0, 0])
    vec = np.array([1, 0])

    logger.debug("\t%s" % str(pos))
    logger.debug("\t%s" % str(vec))

    for line in fileinput.input(files=(args.file)):
        code = line[0]
        num = int(line[1:])
        logger.debug(code + " " + str(num))
        if code == "N":
            pos += np.array([0, 1]) * num
        elif code == "S":
            pos += np.array([0, -1]) * num
        elif code == "E":
            pos += np.array([1, 0]) * num
        elif code == "W":
            pos += np.array([-1, 0]) * num
        elif code == "L":
            vec = rotate_vector(vec, num)
        elif code == "R":
            vec = rotate_vector(vec, -num)
        elif code == "F":
            pos += vec * num
        else:
            assert False

        logger.debug("\t%s" % str(pos))
        logger.debug("\t%s" % str(vec))

    print(int(np.linalg.norm(pos, 1)))


def main2():
    print("--- Part Two ---")
    pos = np.array([0, 0])
    vec = np.array([10, 1])  # waypoint position relative to the ship

    logger.debug("\t%s" % str(pos))
    logger.debug("\t%s" % str(vec))

    for line in fileinput.input(files=(args.file)):
        code = line[0]
        num = int(line[1:])
        logger.debug(code + " " + str(num))
        if code == "N":
            vec += np.array([0, 1]) * num
        elif code == "S":
            vec += np.array([0, -1]) * num
        elif code == "E":
            vec += np.array([1, 0]) * num
        elif code == "W":
            vec += np.array([-1, 0]) * num
        elif code == "L":
            vec = rotate_vector(vec, num)
        elif code == "R":
            vec = rotate_vector(vec, -num)
        elif code == "F":
            pos += vec * num
        else:
            assert False

        logger.debug("\t%s" % str(pos))
        logger.debug("\t%s" % str(vec))

    print(int(np.linalg.norm(pos, 1)))


if __name__ == "__main__":
    main()
    main2()


#   __          __
#  / /____ ___ / /____
# / __/ -_|_-</ __(_-<
# \__/\__/___/\__/___/
#


def test_rotation():
    from pytest import approx

    assert approx([0, 1]) == rotate_vector([1, 0], 90)
    assert approx([0, -1]) == rotate_vector([1, 0], -90)
