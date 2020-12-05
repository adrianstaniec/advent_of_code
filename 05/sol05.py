"""My solution to https://adventofcode.com/2020/day/5"""

import argparse
import logging
import sys

parser = argparse.ArgumentParser()
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


def decode_sead_id(code: str) -> int:
    binary_string = "".join({"F": "0", "B": "1", "L": "0", "R": "1"}[c] for c in code)
    seat_id = int(binary_string, 2)
    logger.debug(f"{code}\t{binary_string}\t{seat_id}")
    return seat_id


def arithmetic_sum(a1, an, n):
    return int((a1 + an) * n / 2)


sum_of_all_seat_ids = arithmetic_sum(0, 2 ** 10 - 1, 2 ** 10)
seat_ids = {*range(2 ** 10)}
logger.debug(sum_of_all_seat_ids)

max_seat_id = -1

with open("input.txt") as f:
    for line in f:
        seat_id = decode_sead_id(line.strip())
        if seat_id > max_seat_id:
            max_seat_id = seat_id
        sum_of_all_seat_ids -= seat_id
        seat_ids.remove(seat_id)
logger.debug(sum_of_all_seat_ids)
logger.info(max_seat_id)
logger.info(seat_ids)


#   __          __
#  / /____ ___ / /____
# / __/ -_|_-</ __(_-<
# \__/\__/___/\__/___/
#


def test1():
    assert decode_sead_id("FBFBBFFRLR") == 357


def test2():
    assert decode_sead_id("BFFFBBFRRR") == 567


def test3():
    assert decode_sead_id("FFFBBBFRRR") == 119


def test4():
    assert decode_sead_id("BBFFBBFRLL") == 820
