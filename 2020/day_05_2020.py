"""Advent of Code 2020 - Day 5: Binary Boarding"""

import sys
import utils_2020


# TODO: Rewerite as a recursion
def find_row_id(bin_id):
    """

    :param bin_id:
    :return:
    """
    id_range = list(range(0, 128))

    for item in bin_id:
        if item == 'F':
            id_range = id_range[:int(len(id_range) / 2)]
        elif item == 'B':
            id_range = id_range[int(len(id_range) / 2):]

    return id_range[0]

# TODO: Rewerite as a recursion
def find_column_id(bin_id):
    """

    :param bin_id:
    :return:
    """
    id_range = list(range(0, 8))

    for item in bin_id:
        if item == 'L':
            id_range = id_range[:int(len(id_range)/2)]
        elif item == 'R':
            id_range = id_range[int(len(id_range)/2):]

    return id_range[0]


def day_05_a(list_data):
    """
    The solution code of AoC 2020 day 5 part 1 problem
    :param list_data:
    :return:
    """
    highest_seat_id = 0

    for bin_id in list_data:
        seat_id = find_row_id(bin_id[:7]) * 8 + find_column_id(bin_id[7:])
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id

    return highest_seat_id

def day_05_b(list_data):
    """
    The solution code of AoC 2020 day 5 part 2 problem
    :param list_data:
    :return:
    """
    seat_ids = list()

    for bin_id in list_data:
        seat_ids.append(find_row_id(bin_id[:7]) * 8 + find_column_id(bin_id[7:]))

    seat_ids.sort()

    for idx, seat_id in enumerate(seat_ids):
        if idx < len(seat_ids)-2:
            if seat_ids[idx+1] != seat_id+1:
                return seat_ids[idx] + 1


def main():
    """
    Open INPUT text file, split the data into list of integers, calculate the answer and print it.
    :return:
    """
    input_data = utils_2020.open_file(sys.argv[1])

    data = input_data.split('\n')

    list_data = [x for x in data[:-1]]

    print('The answer for day 5 part 1 is {}'.format(day_05_a(list_data)))
    print('The answer for day 5 part 2 is {}'.format(day_05_b(list_data)))


if __name__ == '__main__':
    main()
