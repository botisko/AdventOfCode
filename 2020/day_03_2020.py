"""Advent of Code 2020 - Day 3: Toboggan Trajectory"""

import sys
import re
import utils_2020


def process_list_data(list_data, idx_slope_row, idx_slope_column):
    """
    Find no. of 'trees' on predefined slopes
    :param list_data: input data
    :param idx_slope_row: slope index for down movement
    :param idx_slope_column: slope index for right movement
    :return:
    """

    # Get the sizes
    line_len = len(list_data[0])
    list_len = len(list_data)

    # Initial values and indexes
    tree_sum = 0
    idx_list = idx_slope_row
    idx_line = idx_slope_column
    while idx_list < list_len:
        # If we are getting over the line, move to another one
        if idx_line >= line_len:
            idx_line = idx_line % line_len

        # Check if the char is a 'tree'
        if list_data[idx_list][idx_line] == '#':
            tree_sum += 1

        idx_list += idx_slope_row
        idx_line += idx_slope_column

    return tree_sum


def day_03_a(list_data):
    """
    The solution code of AoC 2020 day 3 part 1 problem
    :param list_data:
    :return:
    """

    return process_list_data(list_data, 1, 3)


def day_03_b(list_data):
    """
    The solution code of AoC 2020 day 3 part 2 problem
    :param list_data:
    :return:
    """
    return process_list_data(list_data, 1, 1) * process_list_data(list_data, 1, 3) * process_list_data(list_data, 1,
                                                                                                       5) * \
           process_list_data(list_data, 1, 7) * process_list_data(list_data, 2, 1)


def main():
    """
    Open INPUT text file, split the data into list of integers, calculate the answer and print it.
    :return:
    """
    input_data = utils_2020.open_file(sys.argv[1])

    data = input_data.split('\n')

    list_data = [x for x in data[:-1]]

    print('The answer for day 3 part 1 is {}'.format(day_03_a(list_data)))
    print('The answer for day 3 part 2 is {}'.format(day_03_b(list_data)))


if __name__ == '__main__':
    main()
