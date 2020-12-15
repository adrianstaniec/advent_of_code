"""My solution to https://adventofcode.com/2020/day/15"""

import argparse
import logging
import sys
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", action="store_true")
parser.add_argument("-n", type=int, default=2020)
args = parser.parse_args()


logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.INFO)
if args.debug:
    logger.setLevel(logging.DEBUG)


N = args.n


def main(starting_numbers):
    position = defaultdict(int)
    first_time = True
    for i in range(N):
        next_number: int
        if i < len(starting_numbers):
            next_number = starting_numbers[i]
        else:
            if first_time:
                next_number = 0
        first_time = True if next_number not in position else False
        nnext_number = i - position[next_number] + 1
        position[next_number] = i + 1
        logger.debug(f"Turn {i+1}: {next_number}")
        answer = next_number
        if not first_time:
            next_number = nnext_number
    return answer


if __name__ == "__main__":
    puzzle_input = "7,14,0,17,11,1,2"
    # puzzle_input = "0,3,6"
    starting_numbers = [int(x) for x in puzzle_input.split(",")]
    answer = main(starting_numbers)
    logger.info(answer)
