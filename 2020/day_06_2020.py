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
            # print(answer)
        sum_answers += len(tmp_group)

    return sum_answers

def day_06_b(list_data):
    """
    The solution code of AoC 2020 day 6 part 2 problem
    :param list_data:
    :return:
    """
    sum_answers = 0

    # for group in list_data:
    #     tmp_group = list()
    #     for answers in group:
    #         tmp_group.append(group)
    #         # print(answer)
    #     sum_answers += len(tmp_group)

    # tmp_group = list()
    # # tmp_answ = list()
    # for group in list_data:
    #     if group:
    #         print(group)
    #         tmp_group.append(group)
    #     else:
    #         print(group)
    #         tmp_group.clear()
            # for answer in tmp_group[0]:
            #     print(answer)
            #     # tmp_answ.append([i for i in tmp_group if answer in i])
            # print(tmp_answ)
            # print(answer)
        # sum_answers += len(tmp_group)
    nu_list = list()
    tmp_str = ''
    for idx, item in enumerate(list_data):
        if item != '':
            tmp_str += item + ';'
        else:
            nu_list.append(tmp_str)
            tmp_str = ''

        if idx == len(list_data) - 1:
            nu_list.append(tmp_str)

    for group in nu_list:
        group_answers = group.split(';')[:-1]
        group_answers.sort(key = len)
        print(group_answers)
        for single_answer in group_answers[0]:
            print(single_answer)
            if single_answer in group_answers[1:][:]:
                # print(single_answer)
                pass


        # res = [i for i in answers if answers[1][1] in i]

    bla1 = ['abc']
    bla2 = ['a', 'b', 'c']
    bla3 = ['ab', 'ac']
    bla4 = ['a', 'a', 'a', 'a']
    bla5 = ['b']

    # using list comprehension
    # to get string with substring
    # print([i for i in test_list if subs in i])

    return nu_list


def main():
    """
    Open INPUT text file, split the data into list of integers, calculate the answer and print it.
    :return:
    """
    input_data = utils_2020.open_file(sys.argv[1])

    data = input_data.split('\n')

    list_data = [x for x in data[:-1]]

    print('The answer for day 6 part 1 is {}'.format(day_06_a(list_data)))
    print('The answer for day 6 part 2 is {}'.format(day_06_b(list_data)))


if __name__ == '__main__':
    main()
