"""My solution to http://adventofcode.com/2020/day/18"""

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


class Node:
    def __init__(self, v=None):
        self.value = v
        self.left = None
        self.right = None

    def __repr__(self, level=0):
        s = "  " * level + str(self.value) + "\n"
        for child in [self.left, self.right]:
            if child is not None:
                s += child.__repr__(level + 1)
        return s


def check_if_unnecessary_outer_parens(inp):
    if inp[0] != "(" or inp[-1] != ")":
        return False
    pc = 0
    for i, c in enumerate(inp):
        if c == "(":
            pc += 1
        if c == ")":
            pc -= 1
            if pc == 0:
                if i == len(inp) - 1:
                    return True
                else:
                    return False
    return False


def parse(inp: str):
    # logger.debug(f"p: {inp}")
    node = Node()
    pc = 0  # parentheses counter
    pb = 0  # parentheses beginning
    op_found = False

    if check_if_unnecessary_outer_parens(inp):
        inp = inp[1:-1]

    if inp.isnumeric():
        node.value = int(inp)
        return node

    for i in range(len(inp)):
        i = len(inp) - 1 - i
        c = inp[i]
        if not op_found:
            if c == ")":
                pc += 1
                if pc == 1:
                    pb = i
            elif c == "(":
                pc -= 1
                if pc == 0:
                    node.right = parse(inp[i + 1 : pb])
                continue
            if pc > 0:
                continue
            if c == "+" or c == "*":
                node.value = c
                op_found = True
            elif c.isnumeric():
                node.right = Node(int(c))  # NOTE: works only for operands < 10
        else:
            node.left = parse(inp[: i + 1])
            break
    return node


def calculate(node):
    # logger.debug(f"c: {node.value}")
    if node.value == "*":
        return calculate(node.left) * calculate(node.right)
    elif node.value == "+":
        return calculate(node.left) + calculate(node.right)
    else:
        assert type(node.value) == int, f"Op is {node.value}"
        return node.value


def eval(inp):
    logger.debug(f"Expression: {inp}")
    inp = inp.strip().replace(" ", "")
    node = parse(inp)
    logger.debug(node)
    result = calculate(node)
    logger.debug(f"Total: {result}")
    return result


if __name__ == "__main__":
    results = [eval(line.strip()) for line in fileinput.input(files=(args.input))]
    print('--- Part One ---')
    print(sum(results))
