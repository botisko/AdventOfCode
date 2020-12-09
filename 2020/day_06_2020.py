"""Advent of Code 2020 - Day 6: Custom Customs"""

import sys
import utils_2020

def process_list_data(list_data):
    """
    Create a list of passports
    :param list_data: input data
    :return: processed data
    """
    nu_list = list()

    tmp_str = ''
    for idx, item in enumerate(list_data):
        if item != '':
            tmp_str += item
        else:
            nu_list.append(tmp_str)
            tmp_str = ''

        if idx == len(list_data) - 1:
            nu_list.append(tmp_str)

    return nu_list

def day_06_a(list_data):
    """
    The solution code of AoC 2020 day 6 part 1 problem
    :param list_data:
    :return:
    """

    processed_data = process_list_data(list_data)

    sum_answers = 0

    for group in processed_data:
        tmp_group = set()
        for answer in group:
            tmp_group.add(answer)
        sum_answers += len(tmp_group)

    return sum_answers


def day_06_b():
    """
    The solution code of AoC 2020 day 6 part 2 problem
    :param list_data:
    :return:
    """
    # Inspired by u/mirth23
    # https://www.reddit.com/r/adventofcode/comments/k9eumt/2020_day_6_part_2_python_help_me_be_more_pythonic/
    answers = 0
    with open('day_06_input') as f:
        for group in f.read().split("\n\n"):
            inter = set.intersection(*[set(l) for l in group.split("\n")])
            answers += len(inter)
    return(answers)


def main():
    """
    Open INPUT text file, split the data into list of integers, calculate the answer and print it.
    :return:
    """
    input_data = utils_2020.open_file(sys.argv[1])

    data = input_data.split('\n')

    list_data = [x for x in data[:-1]]

    print('The answer for day 6 part 1 is {}'.format(day_06_a(list_data)))
    print('The answer for day 6 part 2 is {}'.format(day_06_b()))

if __name__ == '__main__':
    main()
