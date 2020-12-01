"""Advent of Code 2018 - Day 1: Chronal Calibration"""

import sys
import utils_2018


def aoc2018_day_01_a(int_data):
    """The solution code of AoC 2018 day 1 part 1 problem"""
    answer = 0

    for x in int_data:
        answer += x

    return answer


def aoc2018_day_01_b(int_data):
    """The solution code of AoC 2018 day 1 part 2 problem"""
    answer = 0

    partial_sum = set()

    freq_found = False

    while freq_found is False:
        for x in int_data:
            answer += x

            if answer not in partial_sum:
                partial_sum.add(answer)
            else:
                freq_found = True
                break

    return answer


def main():
    """Open INPUT text file, split the data into \
    list of integers, calculate the answer and print it."""
    data = aoc2018_utils.open_file(sys.argv[1])

    list_data = data.split('\n')

    int_data = [int(x) for x in list_data[:-1]]

    print('The answer for day 1 part 1 is {}'.format(aoc2018_day_01_a(int_data)))
    print('The answer for day 1 part 2 is {}'.format(aoc2018_day_01_b(int_data)))


if __name__ == '__main__':
    main()
