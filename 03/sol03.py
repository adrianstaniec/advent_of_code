"""My answer to https://adventofcode.com/2020/day/3

Options:
    --debug  Show debug outout.
"""

import math

#    __               _
#   / /__  ___ ____ _(_)__  ___ _
#  / / _ \/ _ `/ _ `/ / _ \/ _ `/
# /_/\___/\_, /\_, /_/_//_/\_, /
#        /___//___/       /___/
import logging
import sys

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.INFO)

#
#  ___ ________ ____
# / _ `/ __/ _ `(_-<
# \_,_/_/  \_, /___/
#         /___/
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", action="store_true")
args = parser.parse_args()
if args.debug:
    logger.setLevel(logging.DEBUG)

#            __                     __            __
#  _______  / /__  ____  ___  __ __/ /____  __ __/ /_
# / __/ _ \/ / _ \/ __/ / _ \/ // / __/ _ \/ // / __/
# \__/\___/_/\___/_/    \___/\_,_/\__/ .__/\_,_/\__/
#                                   /_/
class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


#               __
#  _______  ___/ /__
# / __/ _ \/ _  / -_)
# \__/\___/\_,_/\__/
#


def count_trees(slope, speed=1):
    n_trees = 0
    x_pos = 0
    y_pos = 0
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            if y_pos % speed != 0:
                logger.debug(line + bcolors.WARNING + line + bcolors.ENDC)
            else:
                length = len(line)
                loc_pos = x_pos % length
                logger.debug(
                    line[:loc_pos]
                    + bcolors.FAIL
                    + line[loc_pos]
                    + bcolors.ENDC
                    + line[loc_pos + 1 :]
                    + bcolors.WARNING
                    + line
                    + bcolors.ENDC
                )
                if line[loc_pos] == "#":
                    n_trees += 1
                x_pos += slope
            y_pos += 1
    return n_trees


logger.info(count_trees(3))

print("--- Part Two ---")
logger.info(
    math.prod(
        count_trees(slope, speed)
        for slope, speed in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    )
)
