"""Advent of Code 2022 - Day 1: Calorie Counting"""

import sys
import utils


def day_01_a(input_data):
    """
    The solution code of AoC 2022 day 1 part 1 problem
    :return:
    """
    max_elf = 0
    actual_elf = 0
    # Run through the input data with calories
    for calories in input_data:
        # If switching to next elf, compare the actual elf with max calories
        if calories.isdigit() is False:
            if actual_elf > max_elf:
                max_elf = actual_elf
            actual_elf = 0
        else:
            actual_elf += int(calories)

    return max_elf


def day_01_b(input_data):
    """
    The solution code of AoC 2022 day 1 part 2 problem
    :return:
    """
    list_of_elves = list()
    actual_elf = 0
    # Run through the input data with calories
    for calories in input_data:
        # If switching to next elf, compare the actual elf with max calories
        if calories.isdigit() is False:
            list_of_elves.append(actual_elf)
            actual_elf = 0
        else:
            actual_elf += int(calories)

    # Sort the elves by calories in desc order
    sorted_elves_list = sorted(list_of_elves, reverse=True)

    # Calculate top 3 elves' calories
    return sum(sorted_elves_list[0:3])


def main():
    """
    Open INPUT text file, split the data into list of integers, calculate the answer and print it.
    :return:
    """
    data = utils.open_file(sys.argv[1])

    list_data = data.split('\n')

    print('The answer for day 1 part 1 is {}'.format(day_01_a(list_data)))
    print('The answer for day 1 part 2 is {}'.format(day_01_b(list_data)))


if __name__ == '__main__':
    main()
