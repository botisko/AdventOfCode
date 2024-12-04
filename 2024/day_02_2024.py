"""Advent of Code 2024 - Day 2: Red-Nosed Reports"""

import sys

from numpy.lib.function_base import iterable

import utils


def day_02_a(reports):
    """
    The solution code of AoC 2024 day 2 part 1 problem
    :return:
    """
    safe_reports = 0

    for report in reports:
        sorted_report = sorted(report)
        rev_sorted_report = sorted(report, reverse=True)

        # Select only reports which are ascending/descending and doesn't contain two (or more) same numbers
        if (report == sorted_report or report == rev_sorted_report) and \
                len(report) == len(set(report)):

            # Check if the difference between two adjacent numbers is between 1 and 3
            for idx, no in enumerate(report):
                try:
                    if not 1 <= abs(no - report[idx+1]) <= 3:
                        break
                    else:
                        continue
                except IndexError:
                    safe_reports += 1

    return safe_reports

def day_02_b(reports):
    """
    The solution code of AoC 2024 day 2 part 2 problem2
    :return:
    """

    return None


def main():
    """
    Open INPUT text file, split the data into list of integers, calculate the answer and print it.
    :return:
    """
    data = utils.open_file(sys.argv[1])

    list_data = data.split('\n')

    # Process the input data
    reports = list()

    for level in list_data:
        reports.append([int(x) for x in level.split(" ")])

    print('The answer for day 2 part 1 is {}'.format(day_02_a(reports)))
    print('The answer for day 2 part 2 is {}'.format(day_02_b(reports)))


if __name__ == '__main__':
    main()
