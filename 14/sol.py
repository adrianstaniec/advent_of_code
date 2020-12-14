"""My solution to https://adventofcode.com/2020/day/14"""
import fileinput


def apply_string_mask(smask, num):
    force_zero_mask = int(smask.replace("X", "1"), 2)
    num = num & force_zero_mask
    force_one_mask = int(smask.replace("X", "0"), 2)
    num = num | force_one_mask
    return num


def main():
    mem = {}
    smask = "X" * 36
    for line in fileinput.input():
        line = line.strip()
        print(line)
        if line[:4] == "mask":
            smask = line.split()[-1]
        else:
            address, _, num = line.split()
            mem[address] = apply_string_mask(smask, int(num))

    print(sum(mem.values()))


if __name__ == "__main__":
    main()
