import argparse
import dataclasses

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--debug", action="store_true")
args = parser.parse_args()

filename = "example.txt" if args.debug else "input.txt"


@dataclasses.dataclass
class Instruction:
    op: str
    number: int = 0
    visited: bool = False


print("--- Part One ---")

program = []
with open(filename) as f:
    for line in f:
        line = line.strip().split()
        program.append(Instruction(line[0], int(line[1])))

accumulator = 0
i = 0
while not program[i].visited:
    program[i].visited = True
    if program[i].op == "nop":
        i += 1
    elif program[i].op == "acc":
        accumulator += program[i].number
        i += 1
    else:
        assert program[i].op == "jmp"
        i += program[i].number
print(accumulator)


print("--- Part Two ---")

raise NotImplementedError

for i in range(len(program)):
    program[i].visited = False

accumulator = 0
i = 0
prev_i = -1
while not program[i].visited:
    print(f'- {i}')
    program[i].visited = True
    if program[i].op == "nop":
        prev_i = i
        i += 1
    elif program[i].op == "acc":
        accumulator += program[i].number
        prev_i = i
        i += 1
    else:
        assert program[i].op == "jmp"
        prev_i = i
        i += program[i].number
print(accumulator)
print(prev_i)
print(i)

print("--- Test ---")

for i in range(len(program)):
    program[i].visited = False
from icecream import ic
# program[518].op = "nop"
# program[454].op = "nop"
# program[8].op = "jmp"

accumulator = 0
i = 0
prev_i = -1
j=0
while True:
    print(f"{j}\t{i}\t{program[i]}")
    program[i].visited = True
    if program[i].op == "nop":
        prev_i = i
        i += 1
    elif program[i].op == "acc":
        accumulator += program[i].number
        prev_i = i
        i += 1
    else:
        assert program[i].op == "jmp"
        prev_i = i
        i += program[i].number
    j = j + 1
    if j > 500:
        break
print(accumulator)
print(prev_i)
print(i)
