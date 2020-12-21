"""My solution to https://adventofcode/2020/day/19"""

# Observations:
# - the only rules that do not reference other rules are single character strings
# - we could generate a set all possible valid codes but that might be a lot
# - its a lot but it works fast enough


import fileinput
import argparse
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


#               __
#  _______  ___/ /__
# / __/ _ \/ _  / -_)
# \__/\___/\_,_/\__/
#

def do_list(rules, li, valids):
    for el in li:
        if rules[el][0] == ["a"]:
            valids = {prefix + "a" for prefix in valids}
        elif rules[el][0] == ["b"]:
            valids = {prefix + "b" for prefix in valids}
        else:
            if len(rules[el]) == 2:
                valids = do_alt(rules, rules[el], valids)
            elif len(rules[el]) == 1:
                valids = do_list(rules, rules[el][0], valids)
            else:
                assert False

    return valids


def do_alt(rules, alt, valids):
    valids1 = do_list(rules, alt[0], valids)
    valids2 = do_list(rules, alt[1], valids)
    return valids1 | valids2


rules = {}
stage = "read_rules"
n_valid_msgs = 0

for line in fileinput.input(files=(args.input)):
    logger.debug(line[:-1])
    if stage == "read_rules":
        if line == "\n":
            stage = "read_msgs"
            valid_msgs = do_list(rules, rules["0"][0], {""})
        else:
            f, s = line.strip().split(":")
            rules[f] = []
            for subrule in s.split("|"):
                rules[f].append([r.replace('"', "") for r in subrule.split()])

    elif stage == "read_msgs":
        msg = line.strip()
        if msg in valid_msgs:
            n_valid_msgs += 1

logger.debug(f"{rules=}")
logger.debug(f"{valid_msgs=}")
print('--- Part One ---')
print(f"{n_valid_msgs=}")
