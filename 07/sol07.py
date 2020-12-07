"""My solution to https://adventofcode.com/2020/day/7"""

from typing import Tuple
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str, default='input.txt')
args = parser.parse_args()


FILENAME = args.input
COLOR_IN_QUESTION = "shiny gold"


def split_number_and_color(phrase) -> Tuple[int, str]:
    words = phrase.split()
    if words[0].isnumeric():
        number = int(words[0])
    else:
        number = 0
    return number, " ".join(words[1:])


def parse_input_and_build_a_graph(filename):
    graph = {}
    with open(filename) as f:
        for line in f:
            # remove fluff
            line = (
                line.strip().replace(" bags", "").replace(" bag", "").replace(".", "")
            )
            outer_color, inner_colors = line.split(" contain ")
            graph[outer_color] = [
                split_number_and_color(bag) for bag in inner_colors.split(", ")
            ]
    return graph


def can_color_a_contain_color_b(color_a, color_b, graph):
    """check if bag of color_a can contain a bag of color_b, according to graph"""
    if color_a == "other":
        return False
    for number, inner_color in graph[color_a]:
        if inner_color == color_b:
            return True
        if can_color_a_contain_color_b(inner_color, color_b, graph):
            return True
    return False


print("--- Part One ---")

graph = parse_input_and_build_a_graph(FILENAME)

possible_containing_colors = set()
for k in graph:
    if can_color_a_contain_color_b(k, COLOR_IN_QUESTION, graph):
        possible_containing_colors.add(k)
print(len(possible_containing_colors))

print("--- Part Two ---")


def count_bags(color, graph):
    if color == "other":
        return 0
    sum = 0
    for n, c in graph[color]:
        sum = sum + n + n * count_bags(c, graph)
    return sum


print(count_bags(COLOR_IN_QUESTION, graph))
