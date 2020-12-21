import argparse
import fileinput
from itertools import chain

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", action="store_true")
parser.add_argument("-i", "--input")
args = parser.parse_args()


def main():
    cands = {}
    all_ingredients = []
    for line in fileinput.input(files=(args.input)):
        ingredients, allergens = line[:-2].split(' (contains ')
        ingredients = ingredients.split()
        all_ingredients += ingredients
        allergens = allergens.split(', ')
        for al in allergens:
            if al in cands:
                cands[al] &= set(ingredients)
            else:
                cands[al] = set(ingredients)
        for al in allergens:
            if len(cands[al]) == 1:
                for k in cands:
                    if k != al:
                        cands[k] -= cands[al]

    print(cands)
    print(f'{len(set(all_ingredients))=}')
    print(f'{len(set(cands))=}')
    non_alergic_ings = set(all_ingredients) - set(chain.from_iterable(cands.values()))
    print(f'{non_alergic_ings}=')
    n_non_alergic_ings_appearances = sum(1 for ing in all_ingredients if ing in non_alergic_ings)
    print('--- Part One ---')
    print(n_non_alergic_ings_appearances)


if __name__ == "__main__":
    main()
