"""Advent of Code 2022 - Day 4: Camp Cleanup"""

import sys
import utils


def day_04_a(input_data):
    """
    The solution code of AoC 2022 day 4 part 1 problem
    :return:
    """
    fully_overlapping = 0

    for assignment in input_data:
        # Split the assignment
        elves_assignment = assignment.split(",")
        # Get the assignment range for each elf
        first_elf_range = elves_assignment[0].split("-")
        second_elf_range = elves_assignment[1].split("-")
        # Create an assignment list for each elf
        first_elf = list(range(int(first_elf_range[0]), int(first_elf_range[1])+1))
        second_elf = list(range(int(second_elf_range[0]), int(second_elf_range[1])+1))

        # Find out if any of the assignments fully overlap
        if len(first_elf) >= len(second_elf):
            if set(first_elf) >= set(second_elf):
                fully_overlapping += 1
        else:
            if set(first_elf) < set(second_elf):
                fully_overlapping += 1

    return fully_overlapping


def day_04_b(input_data):
    """
    The solution code of AoC 2022 day 4 part 2 problem
    :return:
    """
    partly_overlapping = 0

    for assignment in input_data:
        # Split the assignment
        elves_assignment = assignment.split(",")
        # Get the assignment range for each elf
        first_elf_range = elves_assignment[0].split("-")
        second_elf_range = elves_assignment[1].split("-")
        # Create an assignment list for each elf
        first_elf = list(range(int(first_elf_range[0]), int(first_elf_range[1])+1))
        second_elf = list(range(int(second_elf_range[0]), int(second_elf_range[1])+1))

        # Find out if any of the assignments partly overlap
        if any([x for x in first_elf if x in second_elf]):
            partly_overlapping += 1

    return partly_overlapping


def main():
    """
    Open INPUT text file, split the data into list of integers, calculate the answer and print it.
    :return:
    """
    data = utils.open_file(sys.argv[1])

    list_data = data.split('\n')

    print('The answer for day 4 part 1 is {}'.format(day_04_a(list_data)))
    print('The answer for day 4 part 2 is {}'.format(day_04_b(list_data)))


if __name__ == '__main__':
    main()
