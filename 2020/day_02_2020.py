"""Advent of Code 2020 - Day 2: Password Philosophy"""

import sys
import re
import utils_2020


def process_list_data(list_item):
    # Find the no.
    pass_no = re.compile('\d*\-\d*').search(list_item)
    pass_min = pass_no.group(0).split('-')[0]
    pass_max = pass_no.group(0).split('-')[1]

    # Find the char
    pass_char = re.compile('\D:').search(list_item).group(0)[0]

    # Find the string
    pass_string = re.compile(':\ \D*').search(list_item).group(0)[2:]

    return pass_min, pass_max, pass_char, pass_string


def day_02_a(list_data):
    """
    The solution code of AoC 2020 day 2 part 1 problem
    :param list_data:
    :return:
    """

    correct_pass_sum = 0

    for item in list_data:
        pass_min, pass_max, pass_char, pass_string = process_list_data(item)

        # Count the no. of the char in the pass
        if int(pass_min) <= pass_string.count(pass_char) <= int(pass_max):
            correct_pass_sum += 1

    return correct_pass_sum


def day_02_b(list_data):
    """
    The solution code of AoC 2020 day 2 part 2 problem
    :param list_data:
    :return:
    """

    correct_pass_sum = 0

    for item in list_data:
        pass_min, pass_max, pass_char, pass_string = process_list_data(item)

        # Check if the pass is valid
        if len(pass_string) >= int(pass_max):
            if (pass_string[int(pass_min) - 1] == pass_char and pass_string[int(pass_max) - 1] != pass_char) or \
                    (pass_string[int(pass_max) - 1] == pass_char and pass_string[int(pass_min) - 1] != pass_char):
                correct_pass_sum += 1

    return correct_pass_sum


def main():
    """
    Open INPUT text file, split the data into list of integers, calculate the answer and print it.
    :return:
    """
    input_data = utils_2020.open_file(sys.argv[1])

    data = input_data.split('\n')

    list_data = [x for x in data[:-1]]

    print('The answer for day 2 part 1 is {}'.format(day_02_a(list_data)))
    print('The answer for day 2 part 2 is {}'.format(day_02_b(list_data)))


if __name__ == '__main__':
    main()
