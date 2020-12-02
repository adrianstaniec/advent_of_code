""" My solution to: https://adventofcode.com/2020/day/2"""

from collections import Counter


def parse(line):
    policy, password = line.strip().split(": ")
    numbers, letter = policy.split(" ")
    mi, ma = map(int, numbers.split("-"))
    return mi, ma, letter, password


def check_validity(mi, ma, letter, password) -> bool:
    counter = Counter(password)
    return mi <= counter[letter] and counter[letter] <= ma


def check_validity2(mi, ma, letter, password) -> bool:
    try:
        return (password[mi-1] == letter) != (password[ma-1] == letter)
    except:
        return False


print("----------- part 1 ---------")

n_valid_passwords = 0

with open("input.txt") as f:
    for line in f:
        mi, ma, letter, password = parse(line)
        if check_validity(mi, ma, letter, password):
            n_valid_passwords += 1

print(n_valid_passwords)

print("----------- part 2 ---------")

n_valid_passwords = 0

with open("input.txt") as f:
    for line in f:
        mi, ma, letter, password = parse(line)
        if check_validity2(mi, ma, letter, password):
            n_valid_passwords += 1

print(n_valid_passwords)
