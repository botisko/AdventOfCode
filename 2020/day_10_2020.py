"""Advent of Code 2020 - Day 10: Adapter Array"""

import sys
import utils_2020


def day_10_a(list_data):
    """
    The solution code of AoC 2020 day 10 part 1 problem
    :param list_data:
    :return:
    """
    # Make a local list and sort it
    adapter_list = list_data
    adapter_list.sort()

    # List of adapters which are connected
    connected_adapters = list()

    # Connect 1st adapter
    connected_adapters.append(adapter_list[0])

    # Count of the 1's and 3's differencies
    unos = 0
    tres = 0

    # Run through the sorted input joltage data and count the numbers
    for adapter in adapter_list[1:]:
        # print(adapter)
        if adapter == connected_adapters[-1] + 1:
            connected_adapters.append(adapter)
            unos += 1
        elif adapter == connected_adapters[-1] + 3:
            connected_adapters.append(adapter)
            tres += 1

    # Fix the values by adding plus one to each of the count... not sure why though
    return (unos+1)*(tres+1)


def day_10_b(list_data):
    """
    The solution code of AoC 2020 day 10 part 2 problem
    :param list_data:
    :return:
    """
    adapters_list = list()

    tmp_lst = list()
    tmp_lst.append(list_data[0])

    # Last checked adapter
    last_adapter = list_data[0]

    for adapter in list_data[1:]:
        print(adapter)

        if adapter != last_adapter+1:
            adapters_list.append(tmp_lst)
            tmp_lst = []
            tmp_lst.append(adapter)
        else:
            tmp_lst.append(adapter)

        last_adapter = adapter

    print(adapters_list)

    return None


def main():
    """
    Open INPUT text file, split the data into list of integers, calculate the answer and print it.
    :return:
    """
    input_data = utils_2020.open_file(sys.argv[1])

    data = input_data.split('\n')

    list_data = [int(x) for x in data[:-1]]

    print('The answer for day 6 part 1 is {}'.format(day_10_a(list_data)))
    print('The answer for day 6 part 2 is {}'.format(day_10_b(list_data)))


if __name__ == '__main__':
    main()
