"""Advent of Code 2020 - Day 5: Binary Boarding"""

import sys
import utils_2020


def find_seat_id(bin_id, min_range, max_range):
    if len(bin_id) == 1:
        print("Finish him!")
        if bin_id == 'B':
            return max_range
        elif bin_id == 'F':
            return min_range
        else:
            return None
    else:
        print('=============')
        if bin_id[0] == 'B':
            max_range_new = int(max_range/2)
            print("Max range: {0}".format(max_range))
        elif bin_id[0] == 'F':
            min_range_new = int(max_range/2)
            print("Min range: {0}".format(min_range))
        print(bin_id[0])
        print(bin_id[1:])
        print('=============')
        find_seat_id(bin_id[1:], min_range_new, max_range_new)


def day_05_a(list_data):
    """
    The solution code of AoC 2020 day 5 part 1 problem
    :param list_data:
    :return:
    """
    print(list_data)


    for bin_id in list_data:
        find_seat_id(bin_id[0:6], 1, 128)
        break


def day_05_b(list_data):
    """
    The solution code of AoC 2020 day 5 part 2 problem
    :param list_data:
    :return:
    """
    pass


def main():
    """
    Open INPUT text file, split the data into list of integers, calculate the answer and print it.
    :return:
    """
    input_data = utils_2020.open_file(sys.argv[1])

    data = input_data.split('\n')

    list_data = [x for x in data[:-1]]

    print('The answer for day 5 part 1 is {}'.format(day_05_a(list_data)))
    # print('The answer for day 5 part 2 is {}'.format(day_05_b(list_data)))


if __name__ == '__main__':
    main()
