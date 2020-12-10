from collections import Counter

adapters = []

while True:
    try:
        adapters.append(int(input()))
    except Exception as e:
        break

print(adapters)
adapters.sort()
adapters = [0] + adapters + [adapters[-1] + 3]
print(adapters)
diffs = [adapters[i + 1] - adapters[i] for i in range(len(adapters) - 1)]
# diffs = [1] + diffs + [3]
print(diffs)
counter = Counter(diffs)
print(counter)

print("--- Part One ---")

print(counter[1] * counter[3])

print("--- Part Two ---")


def arrangements_from_subsequent_unit_differences(x):
    if 0 <= x and x <= 6:
        return {0: 1, 1: 1, 2: 2, 3: 4, 4: 7, 5: 13, 6: 25}[x]
    else:
        raise NotImplemented


n_arrangements = 1
cnt = 0
for d in diffs:
    if d == 1:
        cnt += 1
    elif d == 3:
        n_arrangements *= arrangements_from_subsequent_unit_differences(cnt)
        cnt = 0
print(n_arrangements)
