"""Advent of Code 2020 - Day 7: Handy Haversacks"""

import sys
import utils_2020

def day_07_a(list_data):
    """
    The solution code of AoC 2020 day 7 part 1 problem
    :param list_data:
    :return:
    """

    primary_bags = set()

    for bag in list_data:
        print(bag)
        if "contain" in bag and "shiny gold" in bag:
            bag = bag.split(" ")[0:2]
            primary_bags.add(' '.join(bag))

    return len(primary_bags)-1


def day_07_b(list_data):
    """
    The solution code of AoC 2020 day 7 part 2 problem
    :param list_data:
    :return:
    """
    return list_data


def main():
    """
    Open INPUT text file, split the data into list of integers, calculate the answer and print it.
    :return:
    """
    input_data = utils_2020.open_file(sys.argv[1])

    data = input_data.split('\n')

    list_data = [x for x in data[:-1]]

    print('The answer for day 6 part 1 is {}'.format(day_07_a(list_data)))
    # print('The answer for day 6 part 2 is {}'.format(day_07_b(list_data)))

if __name__ == '__main__':
    main()
