"""Advent of Code 2020 - Day 7: Handy Haversacks"""

import sys
import re
import utils_2020


def iterate_through_bags(baggage_left, final_bags):
    """

    """
    new_baggage_left = baggage_left.copy()
    schluss = True

    for bag in baggage_left:
        remove_primary = False
        for primary_bag in final_bags.copy():
            if re.compile(".*contain.*" + primary_bag).search(bag):
                final_bags.add(' '.join(bag.split(" ")[0:2]))
                remove_primary = True
                schluss = False

        if remove_primary is True:
            new_baggage_left.remove(bag)

    if schluss:
        print(len(final_bags))
        return final_bags
    else:
        iterate_through_bags(new_baggage_left, final_bags)


def day_07_a(list_data):
    """
    The solution code of AoC 2020 day 7 part 1 problem
    :param list_data:
    :return:
    """

    baggage = list_data.copy()

    final_bags = set()

    regex_shiny_primary = re.compile(".*contain.*shiny gold")
    regex_shiny_gold = re.compile("^shiny gold.*")

    # Split shiny gold related bags and the rest
    baggage_primary = [' '.join(y.split(" ")[0:2]) for y in baggage if regex_shiny_primary.search(y)]
    baggage_left = [y for y in baggage if not regex_shiny_primary.search(y) or regex_shiny_gold.search(y)]

    final_bags.update(baggage_primary)

    total_bags = iterate_through_bags(baggage_left, final_bags)


def day_07_b(list_data):
    """
    The solution code of AoC 2020 day 7 part 2 problem
    :param list_data:
    :return:
    """
    baggage = list_data.copy()

    final_bags = set()

    regex_shiny_gold = re.compile("^shiny gold.*")

    # Split shiny gold related bags and the rest
    baggage_primary = [y for y in baggage if regex_shiny_gold.search(y)]
    baggage_left = [y for y in baggage if not regex_shiny_gold.search(y)]

    print(baggage_primary)
    print(baggage_left)

    # final_bags.update(baggage_primary)

    # total_bags = iterate_through_bags(baggage_left, final_bags)


def main():
    """
    Open INPUT text file, split the data into list of integers, calculate the answer and print it.
    :return:
    """
    input_data = utils_2020.open_file(sys.argv[1])

    data = input_data.split('\n')

    list_data = [x for x in data[:-1]]

    print('The answer for day 6 part 1 is {}'.format(day_07_a(list_data)))
    print('The answer for day 6 part 2 is {}'.format(day_07_b(list_data)))


if __name__ == '__main__':
    main()
