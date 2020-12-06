"""My solution to https://adventofcode.com/2020/day/6"""

sum_of_counts = 0
with open('input.txt') as f:
    s = set()
    for line in f:
        if line == '\n':
            count = len(s)
            sum_of_counts += count
            s = set()
        else:
            s = s | set(line.strip())
    count = len(s)
    sum_of_counts += count
    s = set()
print(sum_of_counts)

print("--- Part Two ---")

sum_of_counts = 0
first = True
with open('input.txt') as f:
    for line in f:
        if line == '\n':
            count = len(s)
            sum_of_counts += count
            first = True
        else:
            if first:
                s = set(line.strip())
                first = False
            else:
                s = s & set(line.strip())
    count = len(s)
    sum_of_counts += count
    s = set()
print(sum_of_counts)
