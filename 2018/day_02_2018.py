"""Advent of Code 2018 - Day 2: Inventory Management System"""

import sys
import aoc2018_utils


def aoc2018_day_02_a(list_data):
    """The solution code of AoC 2018 day 2 part 1 problem"""
    twos = 0
    threes = 0

    for box_id in list_data:
        current_box = {}
        for letter in box_id:
            if letter not in current_box:
                current_box[letter] = 1
            else:
                current_box[letter] += 1

        # Find if there is a key (letter) in current box ID with appearance 2 and/or 3
        current_twos = [key for (key, value) in current_box.items() if value is 2]
        current_threes = [key for (key, value) in current_box.items() if value is 3]

        # If 2s or 3s are found add them to their sums
        if current_twos:
            twos += 1

        if current_threes:
            threes += 1

    return twos * threes


def aoc2018_day_02_b(list_data):
    """The solution code of AoC 2018 day 2 part 2 problem"""

    print(list_data)

    # Run through the whole list
    for i in range(1, len(list_data)):
        for j in range(1, len(list_data-i)):
            for l in range(1, len(list_data[i])):
                if not list_data[i][l] == list_data[j][l]:
                    continue

    return True


def main():
    """Open INPUT text file, split the data into \
    list of integers, calculate the answer and print it."""
    data = aoc2018_utils.open_file(sys.argv[1])

    list_data = data.split('\n')

    # print('The answer for day 2 part 1 is {}'.format(aoc2018_day_02_a(list_data)))

    print('The answer for day 2 part 2 is {}'.format(aoc2018_day_02_b(list_data)))


if __name__ == '__main__':
    main()
