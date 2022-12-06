"""Advent of Code 2022 - Day 6: Tuning Trouble"""

import sys
import utils


def day_06_a(list_data):
    """
    The solution code of AoC 2022 day 6 part 1 problem
    :return:
    """
    # Go through the input string
    for idx, char in enumerate(list_data):
        # Store 4 chars into a set
        set_data = {*list_data[idx:idx + 4]}

        # If the 4 chars are unique, return the start-of-packet marker index
        if len(set_data) == 4:
            return idx + 4
        else:
            continue


def day_06_b(list_data):
    """
    The solution code of AoC 2022 day 6 part 2 problem
    :return:
    """
    # Go through the input string
    for idx, char in enumerate(list_data):
        # Store 14 chars into a set
        set_data = {*list_data[idx:idx + 14]}

        # If the 14 chars are unique, return the start-of-message marker index
        if len(set_data) == 14:
            return idx + 14
        else:
            continue


def main():
    """
    Open INPUT text file, split the data into list of integers, calculate the answer and print it.
    :return:
    """
    data = utils.open_file(sys.argv[1])

    print('The answer for day 6 part 1 is {}'.format(day_06_a(data)))
    print('The answer for day 6 part 2 is {}'.format(day_06_b(data)))


if __name__ == '__main__':
    main()
