"""My solution to https://adventofcode.com/2020/day/13"""

import argparse
import fileinput
import logging
import sys

import numpy as np

#    __       __
#   / /  ___ / /__  ___ _______
#  / _ \/ -_) / _ \/ -_) __(_-<
# /_//_/\__/_/ .__/\__/_/ /___/
#           /_/

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("-d", "--debug", action="store_true")
args = parser.parse_args()

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.INFO)
if args.debug:
    logger.setLevel(logging.DEBUG)


def visualization(busses, timestamp):
    if not args.debug:
        return

    from colorama import init, Fore, Style

    init()

    print("time".ljust(16), end="\t")
    for b in busses:
        print(b, end="\t")
    print("")

    for i in range(-20, 20):
        if i == 0:
            print(Fore.YELLOW, end="")
        else:
            print(Style.RESET_ALL, end="")
        t = timestamp + i
        print(f"{t:<16}", end="\t")
        for b in busses:
            if t % b == 0:
                print("D", end="\t")
            else:
                print(".", end="\t")
        print("")


#               __
#  _______  ___/ /__
# / __/ _ \/ _  / -_)
# \__/\___/\_,_/\__/
#


def main():
    logger.info("--- Part One ---")
    for i, line in enumerate(fileinput.input(files=(args.input))):
        if i == 0:
            timestamp = int(line)
        if i == 1:
            busses = [int(b) for b in line.strip().split(",") if b != "x"]
            bussesx = [int(b) if b != "x" else 0 for b in line.strip().split(",")]
    logger.debug(timestamp)
    logger.debug(busses)
    minutes_till_depature = [
        b - timestamp % b if timestamp % b > 0 else 0 for b in busses
    ]
    logger.debug(minutes_till_depature)

    visualization(busses, timestamp)
    earliest_bus_index = np.argmin(minutes_till_depature)
    ans1 = busses[earliest_bus_index] * minutes_till_depature[earliest_bus_index]
    logger.info(f"{ans1=}")

    logger.info("--- Part Two ---")
    bus_offset = {}
    for i in range(len(bussesx)):
        if bussesx[i] != 0:
            bus_offset[bussesx[i]] = i

    # start with stepping using max bus id
    step = max(busses)
    step_offset = np.argmax(bussesx)
    logger.debug(f"{step=}")
    logger.debug(f"{step_offset=}")
    # for t in range(1, 2000000):  # naive brute force
    i = 0
    t = 0
    t = t - step_offset
    while True:
        i += 1
        t += step
        logger.debug(f"-- t = {t} -- it {i} -- step {step}")
        dbg_str = ""
        found = True
        for bus, offset in bus_offset.items():
            if (t + offset) % bus != 0:
                found = False
            else:
                # increase step by factor of previously unmatched bus
                if step % bus != 0:
                    step *= bus
                dbg_str += f"{bus}, "
        logger.debug(dbg_str)
        if found:
            visualization(busses, t)
            ans2 = t
            logger.info(f"{ans2=}")
            break


if __name__ == "__main__":
    main()
