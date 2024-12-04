"""Advent of Code 2024 - Day 4: Ceres Search"""

import sys

from numpy.lib.function_base import iterable

import utils


def day_04_a(list_data):
    """
    The solution code of AoC 2024 day 4 part 1 problem
    :return:
    """
    occurences = 0

    for idx_line, line in enumerate(list_data):
        # Find XMAS and SAMX occurences in the current line
        occurences += line.count("XMAS")
        occurences += line.count("SAMX")
        for idx_char, char in line:
            # Find if there is diagonal occurence
            if char == "X":
                pass
            else:
                continue


    return occurences

def day_04_b(reports):
    """
    The solution code of AoC 2024 day 4 part 2 problem
    :return:
    """
    safe_reports = 0

    return safe_reports


def main():
    """
    Open INPUT text file, split the data into list of integers, calculate the answer and print it.
    :return:
    """
    data = utils.open_file(sys.argv[1])

    list_data = data.split('\n')

    print(list_data)

    print('The answer for day 4 part 1 is {}'.format(day_04_a(list_data)))
    # print('The answer for day 4 part 2 is {}'.format(day_04_b(list_data)))


if __name__ == '__main__':
    main()
