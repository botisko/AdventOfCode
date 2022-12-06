"""Advent of Code 2022 - Day 3: Rucksack Reorganization"""

import sys
import utils
import string


def get_priorities():
    """
    This function creates a dict of alphabet letters priorities
    :return:
    """
    # Create a lowercase and uppercase alphabet
    alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    priorities = dict()

    priority = 1

    # Fill the priorities' dict with alphabet letters and theirs priority
    for letter in alphabet:
        priorities[letter] = priority
        priority += 1

    return priorities


def day_03_a(input_data):
    """
    The solution code of AoC 2022 day 3 part 1 problem
    :return:
    """
    # Get priorities dict
    priorities = get_priorities()

    # Count the single items priority
    single_items_priority = 0

    for rucksack in input_data:
        # Split the rucksack into two compartments
        first_compartment = rucksack[:int((len(rucksack) / 2))]
        second_compartment = rucksack[int(len(rucksack) / 2):]

        # Use list comprehension to filter out the one common item
        the_item = [x for x in first_compartment if x in second_compartment]

        single_items_priority += priorities[the_item[0]]

    return single_items_priority


def day_03_b(input_data):
    """
    The solution code of AoC 2022 day 3 part 2 problem
    :return:
    """
    # Get priorities dict
    priorities = get_priorities()
    badge_priority = 0

    # Split the input into groups of 3
    input_groups = [input_data[i:i + 3] for i in range(0, len(input_data), 3)]

    # Count the badges priority
    for group in input_groups:
        # Use list comprehension to filter out the badge (a common item in a group of 3)
        the_badge = [x for x in group[0] if x in group[1] if x in group[2]]

        badge_priority += priorities[the_badge[0]]

    return badge_priority


def main():
    """
    Open INPUT text file, split the data into list of integers, calculate the answer and print it.
    :return:
    """
    data = utils.open_file(sys.argv[1])

    list_data = data.split('\n')

    print('The answer for day 3 part 1 is {}'.format(day_03_a(list_data)))
    print('The answer for day 3 part 2 is {}'.format(day_03_b(list_data)))


if __name__ == '__main__':
    main()
