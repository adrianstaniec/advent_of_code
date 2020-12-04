import argparse
import string
import sys
from typing import List, Dict

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", action="store_true")
args = parser.parse_args()
input_file = "input.txt"

if args.debug:
    input_file = "debug_input.txt"


#               __
#  _______  ___/ /__
# / __/ _ \/ _  / -_)
# \__/\___/\_,_/\__/
#


def validate_passport(passport: Dict[str, str]) -> bool:
    required_fields = {"ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"}
    fields = set(passport)
    if len(required_fields & fields) == len(required_fields):
        return True
    else:
        return False


n_valid_passports = 0

with open(input_file) as f:
    passport = {}
    for line in f:
        if line == "\n":
            if validate_passport(passport):
                n_valid_passports += 1
            passport = {}
        for field in line.strip().split():
            k, v = field.split(":")
            passport[k] = v
    if validate_passport(passport):
        n_valid_passports += 1

print(f"ans: {n_valid_passports}")


print("--- Part Two ---")


def validate_passport2(passport: Dict[str, str]) -> bool:
    required_fields = {"ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"}
    fields = set(passport)
    if len(required_fields & fields) != len(required_fields):
        return False

    birth_year = passport["byr"]
    if len(birth_year) != 4:
        return False
    if int(birth_year) < 1920 or 2002 < int(birth_year):
        return False

    issue_year = passport["iyr"]
    if len(issue_year) != 4:
        return False
    if int(issue_year) < 2010 or 2020 < int(issue_year):
        return False

    expiration_year = passport["eyr"]
    if len(expiration_year) != 4:
        return False
    if int(expiration_year) < 2020 or 2030 < int(expiration_year):
        return False

    height = passport["hgt"]
    if height[-2:] == "cm":
        height = int(height[:-2])
        if height < 150 or height > 193:
            return False
    elif height[-2:] == "in":
        height = int(height[:-2])
        if height < 59 or height > 76:
            return False
    else:
        return False

    hair = passport["hcl"]
    if hair[0] != "#":
        return False
    for c in hair[1:]:
        if c not in string.hexdigits:
            return False

    eye = passport["ecl"]
    if eye not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
        return False

    passport_id = passport['pid']
    if len(passport_id) != 9:
        return False
    for n in passport_id:
        if n not in string.digits:
            return False

    return True


n_valid_passports = 0

with open(input_file) as f:
    passport = {}
    for line in f:
        if line == "\n":
            if validate_passport2(passport):
                n_valid_passports += 1
            passport = {}
        for field in line.strip().split():
            k, v = field.split(":")
            passport[k] = v
    if validate_passport2(passport):
        n_valid_passports += 1

print(f"ans: {n_valid_passports}")


