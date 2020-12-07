"""My solution to https://adventofcode.com/2020/day/7"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", action="store_true")
args = parser.parse_args()

FILE = "example.txt" if args.debug else "input.txt"


def remove_number(phrase):
    return " ".join(phrase.split()[1:])


graph = {}
with open(FILE) as f:
    for line in f:
        # remove fluff
        line = line.strip().replace(" bags", "").replace(" bag", "").replace(".", "")
        outer_color, inner_colors = line.split(" contain ")
        inner_colors = [remove_number(bag) for bag in inner_colors.split(", ")]
        graph[outer_color] = inner_colors

possible_containing_colors = set()
KEY = "shiny gold"


def can_color_a_contain_color_b(color_a, color_b, graph):
    """check if bag of color_a can contain a bag of color_b, according to graph"""
    if color_a == 'other':
        return False
    for inner_color in graph[color_a]:
        if inner_color == color_b:
            return True
        if can_color_a_contain_color_b(inner_color, color_b, graph):
            return True
    return False


for k in graph.keys():
    if can_color_a_contain_color_b(k, KEY, graph):
        possible_containing_colors.add(k)

print(len(possible_containing_colors))
