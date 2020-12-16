"""My solution to https://adventofcode.com/2020/day/16"""

import argparse
import fileinput
import logging
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", action="store_true")
parser.add_argument("-i", "--input")
args = parser.parse_args()

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.INFO)
if args.debug:
    logger.setLevel(logging.DEBUG)


def parse():
    stage = 1
    rules = {}
    my_ticket = []
    nearby_tickets = []

    for line in fileinput.input(files=(args.input)):
        # rough parsing
        line = line.strip()
        if line == "":
            stage += 1
            continue
        if line[:4] == "your" or line[:4] == "near":
            continue

        # detailed parsing
        if stage == 1:
            field, rest = line.split(":")
            range1, range2 = rest.split(" or ")
            range1min, range1max = map(int, range1.split("-"))
            range2min, range2max = map(int, range2.split("-"))
            rules[field] = ((range1min, range1max), (range2min, range2max))
        elif stage == 2:
            my_ticket = [int(v) for v in line.split(",")]
        else:
            nearby_tickets.append([int(v) for v in line.split(",")])

    logger.debug(f"{rules=}")
    logger.debug(f"{my_ticket=}")
    logger.debug(f"{nearby_tickets=}")
    return rules, my_ticket, nearby_tickets


def valid_with_any_rule(value, rules):
    valid = False
    for range1, range2 in rules.values():
        if range1[0] <= value and value <= range1[1]:
            valid = True
        if range2[0] <= value and value <= range2[1]:
            valid = True
    logger.debug(f"value {value} is valid: {valid}")
    return valid


if __name__ == "__main__":
    rules, my_ticket, nearby_tickets = parse()

    invalid_values = [
        value
        for ticket in nearby_tickets
        for value in ticket
        if not valid_with_any_rule(value, rules)
    ]
    logger.debug(invalid_values)
    print(sum(invalid_values))
