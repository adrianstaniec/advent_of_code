from collections import deque
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i")
parser.add_argument("-n", type=int)
args = parser.parse_args()

input_file = args.i
n = args.n


def is_valid(x, d):
    """Checks is x is valid according to d.

    Valid means that two different numbers from d,
    can be summed up to x.
    """
    # TODO: can be done more efficiently if needed
    for i in d:
        for j in d:
            if i + j == x and i != j:
                return True
    return False


ring = deque(maxlen=n)
i = 0
with open(input_file) as f:
    for line in f:
        x = int(line.strip())
        if i >= n:
            if not is_valid(x, ring):
                break
        ring.append(x)
        i += 1

ans = x
print(ans)


print('--- Part Two ---')

fifo = deque()
with open(input_file) as f:
    for line in f:
        x = int(line.strip())
        fifo.append(x)
        while ans < sum(fifo):
            fifo.popleft()
        if ans == sum(fifo):
            break
print(fifo)
print(min(fifo)+max(fifo))
