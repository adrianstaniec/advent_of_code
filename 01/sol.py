""" My answer to: https://adventofcode.com/2020/day/1 """

import numpy as np
import math

xs = []
with open("input.txt") as f:
    for l in f:
        xs.append(int(l))

xs = np.array(xs)
Xs = xs[:, np.newaxis] + xs[np.newaxis, :]

assert Xs.shape[0] == xs.shape[0]
assert Xs.shape[1] == xs.shape[0]
print(xs)
print(Xs)

idxs = list(zip(*np.where(Xs == 2020)))

assert len(idxs) == math.factorial(2)
assert idxs[0][0] == idxs[1][1]
assert idxs[0][1] == idxs[1][0]
print(idxs)

x1 = xs[idxs[0][0]]
x2 = xs[idxs[0][1]]
ans = x1 * x2

print(f"Answer:  {x1} * {x2} = {ans}")

print("=============================")
print("part2")

Xs = (
    xs[:, np.newaxis, np.newaxis]
    + xs[np.newaxis, :, np.newaxis]
    + xs[np.newaxis, np.newaxis, :]
)

assert Xs.shape[0] == xs.shape[0]
assert Xs.shape[1] == xs.shape[0]
assert Xs.shape[2] == xs.shape[0]
print(Xs)

idxs = list(zip(*np.where(Xs == 2020)))

print(idxs)
assert len(idxs) == math.factorial(3)

x1 = xs[idxs[0][0]]
x2 = xs[idxs[0][1]]
x3 = xs[idxs[0][2]]
ans = x1 * x2 * x3
print(f"Answer:  {x1} * {x2} * {x3} = {ans}")
