"""Advent of Code 2024 - Day 1: Historian Hysteria"""

import sys
import utils


def day_01_a(location_ids_left, location_ids_right):
    """
    The solution code of AoC 2024 day 1 part 1 problem
    :return:
    """
    distance = 0

    for idx, _id in enumerate(location_ids_left):
        distance += abs(_id - location_ids_right[idx])

    return distance

def day_01_b(location_ids_left, location_ids_right):
    """
    The solution code of AoC 2024 day 1 part 2 problem
    :return:
    """
    similarity_score = 0

    for idx, _id in enumerate(location_ids_left):
        similarity_score += _id * location_ids_right.count(_id)

    return similarity_score


def main():
    """
    Open INPUT text file, split the data into list of integers, calculate the answer and print it.
    :return:
    """
    data = utils.open_file(sys.argv[1])

    list_data = data.split('\n')

    # Process the input data
    location_ids_left = list()
    location_ids_right = list()

    # Divide the left/right data into 2 separate lists
    for id in list_data:
        location_ids_left.append(int(id.split(' ')[0]))
        location_ids_right.append(int(id.split(' ')[-1]))

    # Sort the data
    location_ids_left.sort()
    location_ids_right.sort()

    print('The answer for day 1 part 1 is {}'.format(day_01_a(location_ids_left, location_ids_right)))
    print('The answer for day 1 part 2 is {}'.format(day_01_b(location_ids_left, location_ids_right)))


if __name__ == '__main__':
    main()
