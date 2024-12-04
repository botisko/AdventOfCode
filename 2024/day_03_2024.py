"""Advent of Code 2024 - Day 3: Mull It Over"""

import sys
import utils
import re


def day_03_a(input_data):
    """
    The solution code of AoC 2024 day 3 part 1 problem
    :return:
    """
    mul_sum = 0

    # Find all mul(x,y) occurrences
    mul = re.findall(r'mul\(\d+,\d+\)', input_data)

    # Multiply the numbers and add them to the sum
    for numbers in mul:
        mux = (re.findall(r'\d+', numbers))
        mul_sum += int(mux[0]) * int(mux[1])

    return mul_sum


def day_03_b(input_data):
    """
    The solution code of AoC 2024 day 3 part 2 problem
    :return:
    """
    mul_sum = 0

    # Split the input by do()'s
    processed_data = input_data.split("do()")

    for do in processed_data:
        # Split each do line by don't
        dont = do.split("don't()")
        # Find all mul(x,y) occurrences after do() - that means all in a string in the first list item; the next item(s)
        # in the list come(s) after don't()
        mul = re.findall(r'mul\(\d+,\d+\)', dont[0])
        # Multiply the numbers and add them to the sum
        for numbers in mul:
            mux = (re.findall(r'\d+', numbers))
            mul_sum += int(mux[0]) * int(mux[1])

    return mul_sum


def main():
    """
    Open INPUT text file, split the data into list of integers, calculate the answer and print it.
    :return:
    """
    data = utils.open_file(sys.argv[1])

    list_data = data.split('\n')

    input_data = "".join(list_data)

    print('The answer for day 3 part 1 is {}'.format(day_03_a(input_data)))
    print('The answer for day 3 part 2 is {}'.format(day_03_b(input_data)))


if __name__ == '__main__':
    main()
