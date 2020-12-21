"""My solution to https://adventofcode/2020/day/21"""
import argparse
import fileinput
import logging
import sys
from itertools import chain

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", action="store_true")
parser.add_argument("-i", "--input")
args = parser.parse_args()

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.INFO)
if args.debug:
    logger.setLevel(logging.DEBUG)


def main():
    al_to_ings = {}
    all_ingredients = []
    for line in fileinput.input(files=(args.input)):
        ingredients, allergens = line[:-2].split(" (contains ")
        ingredients = ingredients.split()
        all_ingredients += ingredients
        allergens = allergens.split(", ")
        for al in allergens:
            if al in al_to_ings:
                al_to_ings[al] &= set(ingredients)
            else:
                al_to_ings[al] = set(ingredients)
        for al in allergens:
            if len(al_to_ings[al]) == 1:
                for k in al_to_ings:
                    if k != al:
                        al_to_ings[k] -= al_to_ings[al]

    all_allergic_ings = set(chain.from_iterable(al_to_ings.values()))
    all_allergens = set(al_to_ings)
    logger.debug(f"{all_allergic_ings=}")
    logger.debug(f"{all_allergens=}")

    while max(len(ings) for al, ings in al_to_ings.items()) > 1:
        for al in all_allergens:
            if len(al_to_ings[al]) == 1:
                for k in al_to_ings:
                    if k != al:
                        al_to_ings[k] -= al_to_ings[al]

    logger.debug(al_to_ings)
    logger.debug(f"{len(set(all_ingredients))=}")
    logger.debug(f"{len(set(al_to_ings))=}")
    non_alergic_ings = set(all_ingredients) - all_allergic_ings
    logger.debug(f"{non_alergic_ings}=")
    n_non_alergic_ings_appearances = sum(
        1 for ing in all_ingredients if ing in non_alergic_ings
    )
    logger.info("--- Part One ---")
    logger.info(n_non_alergic_ings_appearances)
    for k, v in al_to_ings.items():
        logger.debug(f"{k}\t{v}")

    logger.info("--- Part Two ---")

    ing_to_al = {}
    for al, ings in al_to_ings.items():
        assert len(ings) == 1
        ing = next(iter(ings))
        ing_to_al[ing] = al
    logger.info(",".join(sorted(ing_to_al, key=lambda k: ing_to_al[k])))


if __name__ == "__main__":
    main()
