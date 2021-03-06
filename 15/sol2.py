import argparse
import logging
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", action="store_true")
parser.add_argument("-n", type=int, default=2020)
args = parser.parse_args()


logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.INFO)
if args.debug:
    logger.setLevel(logging.DEBUG)


N = args.n


def main(starting_numbers):
    sequence = [0] * N
    spoken_but_last = set()
    for i in range(N):
        next_number: int
        if i < len(starting_numbers):
            next_number = starting_numbers[i]
        else:
            # if sequence[i-1] in sequence[:i-1]:
            if sequence[i - 1] in spoken_but_last:
                cnt = 0
                for number in reversed(sequence[: i - 1]):
                    cnt += 1
                    if number == sequence[i - 1]:
                        break
                next_number = cnt
            else:
                next_number = 0
        if i > 0:
            spoken_but_last.add(sequence[i - 1])
        sequence[i] = next_number
        logger.debug(f"Turn {i+1}: {next_number}")
    return sequence[-1]


if __name__ == "__main__":
    puzzle_input = "7,14,0,17,11,1,2"
    # puzzle_input = "0,3,6"
    starting_numbers = [int(x) for x in puzzle_input.split(",")]
    answer = main(starting_numbers)
    logger.info(answer)
