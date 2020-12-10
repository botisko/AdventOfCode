"""Advent of Code 2020 - Day 9: Encoding Error"""

import sys
import utils_2020


def day_09_a(list_data, preamble):
    """
    The solution code of AoC 2020 day 9 part 1 problem
    :param list_data:
    :return:
    """

    previous_numbers = list_data[:preamble]

    # Loop through all the numbers
    for x, number in enumerate(list_data[preamble:]):
        stop = True

        for y, fst_num in enumerate(previous_numbers):
            for rest_num in previous_numbers[y + 1:]:
                if int(fst_num) + int(rest_num) == int(number):
                    stop = False
                    break

        if stop is True:
            return number
        else:
            previous_numbers.clear()
            previous_numbers = list_data[x + 1:x + 1 + preamble]


def day_09_b(list_data, inv_number):
    """
    The solution code of AoC 2020 day 9 part 2 problem
    :param list_data:
    :return:
    """

    # print(inv_number)

    previous_numbers = list()

    for idx, fst_number in enumerate(list_data):
        # Add a no. to list of previous no.
        for next_number in list_data[idx:]:
            previous_numbers.append(int(next_number))
            # Check if we're good
            if sum(previous_numbers) > int(inv_number):
                previous_numbers.clear()
                break
            elif sum(previous_numbers) == int(inv_number):
                return min(previous_numbers) + max(previous_numbers)

    return list_data


def main():
    """
    Open INPUT text file, split the data into list of integers, calculate the answer and print it.
    :return:
    """
    input_data = utils_2020.open_file(sys.argv[1])

    data = input_data.split('\n')

    list_data = [x for x in data]

    print('The answer for day 6 part 1 is {}'.format(day_09_a(list_data, 25)))
    print('The answer for day 6 part 2 is {}'.format(day_09_b(list_data, day_09_a(list_data, 25))))


if __name__ == '__main__':
    main()
