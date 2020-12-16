"""My s lution to https://adventofcode.com/2020/day/16"""

import argparse
import fileinput
import logging
import sys
import operator
from math import prod

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


def value_according_to_rule(value, rule):
    range1, range2 = rule
    return (range1[0] <= value and value <= range1[1]) or (
        range2[0] <= value and value <= range2[1]
    )


def valid_with_any_rule(value, rules):
    valid = False
    for range1, range2 in rules.values():
        if range1[0] <= value and value <= range1[1]:
            valid = True
        if range2[0] <= value and value <= range2[1]:
            valid = True
    return valid


def every_field_valid_with_some_rule(ticket, rules):
    for value in ticket:
        if not valid_with_any_rule(value, rules):
            return False
    return True


if __name__ == "__main__":
    rules, my_ticket, nearby_tickets = parse()

    logger.info("--- Part One ---")
    invalid_values = [
        value
        for ticket in nearby_tickets
        for value in ticket
        if not valid_with_any_rule(value, rules)
    ]
    logger.debug(invalid_values)
    logger.info(sum(invalid_values))

    logger.info("--- Part Two ---")

    # discard tickets with invalid values
    logger.debug(len(nearby_tickets))
    nearby_tickets = [
        ticket
        for ticket in nearby_tickets
        if every_field_valid_with_some_rule(ticket, rules)
    ]
    logger.debug(len(nearby_tickets))

    # NOTE: I guess the assumption is that all the remaining nearby tickets are valid
    # but it is certainly not guaranteed by the filtering above

    # start with all possibilities
    n_fields = len(rules)
    col_to_field = {i: set(rules.keys()) for i in range(n_fields)}

    # scan all tickets column by column
    # to rule out classes that don't fit the data
    for col in range(n_fields):
        for ticket in nearby_tickets:
            col_to_field[col] = {
                field
                for field in col_to_field[col]
                if value_according_to_rule(ticket[col], rules[field])
            }

    logger.debug(f"\n{col_to_field=}")

    # if thanks to elimination there is a single canidate per column:
    # store it in figured dict
    # and eliminate that candidate from the set of candidated for all other columns
    # repeat until all columns are figured out
    # NOTE: data is set up in a way that it will work
    figured = {}
    while len(col_to_field) > 0:
        i = min(col_to_field, key=lambda k: len(col_to_field[k]))
        if len(col_to_field[i]) > 1:
            break
        figured[i] = col_to_field[i]
        del col_to_field[i]
        for col in col_to_field:
            col_to_field[col] -= figured[i]

    logger.debug(f"\n{figured=}")

    field_no = {v.pop(): k for k, v in figured.items()}
    logger.debug([my_ticket[v] for k, v in field_no.items() if k.startswith("departure")])
    answer = prod(my_ticket[v] for k, v in field_no.items() if k.startswith("departure"))

    logger.debug(f"\n{field_no=}")
    logger.debug(f"\n{my_ticket=}")
    logger.info(answer)
