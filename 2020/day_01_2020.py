"""Advent of Code 2020 - Day 1: Report Repair"""

import sys
import utils_2020


def day_01_a(int_data):
    """
    The solution code of AoC 2020 day 1 part 1 problem
    :param int_data:
    :return:
    """
    for idx_1, int_1 in enumerate(int_data):
        for idx_2, int_2 in enumerate(int_data):
            if int_1 + int_2 == 2020:
                num_idx_1 = idx_1
                num_idx_2 = idx_2
                break

    return int_data[num_idx_1]*int_data[num_idx_2]


def day_01_b(int_data):
    """
    The solution code of AoC 2020 day 1 part 2 problem
    :param int_data:
    :return:
    """
    for idx_1, int_1 in enumerate(int_data):
        for idx_2, int_2 in enumerate(int_data):
            for idx_3, int_3 in enumerate(int_data):
                if int_1 + int_2 + int_3 == 2020:
                    num_idx_1 = idx_1
                    num_idx_2 = idx_2
                    num_idx_3 = idx_3
                    break

    return int_data[num_idx_1]*int_data[num_idx_2]*int_data[num_idx_3]


def main():
    """
    Open INPUT text file, split the data into list of integers, calculate the answer and print it.
    :return:
    """
    data = utils_2020.open_file(sys.argv[1])

    list_data = data.split('\n')

    int_data = [int(x) for x in list_data[:-1]]

    print('The answer for day 1 part 1 is {}'.format(day_01_a(int_data)))
    print('The answer for day 1 part 2 is {}'.format(day_01_b(int_data)))


if __name__ == '__main__':
    main()
