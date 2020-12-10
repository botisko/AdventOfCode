"""Advent of Code 2020 - Day 8: Handheld Halting"""

import sys
import utils_2020


def day_08_a(list_data):
    """
    The solution code of AoC 2020 day 8 part 1 problem
    :param list_data:
    :return:
    """
    # Immediately before any instruction is executed a second time, what value is in the accumulator?
    acc_value = 0

    instructions_done = list()

    idx = 0

    while True:
        current_instr = list_data[idx]

        if idx in instructions_done:
            break
        else:
            instructions_done.append(idx)

        instr = current_instr.split(" ")

        # Perform instruction
        if instr[0] == "nop":
            idx += 1
        elif instr[0] == "acc":
            if instr[1][0] == "+":
                acc_value += int(instr[1][1:])
            else:
                acc_value -= int(instr[1][1:])
            idx += 1
        elif instr[0] == "jmp":
            if instr[1][0] == "+":
                idx += int(instr[1][1:])
            else:
                idx -= int(instr[1][1:])

    return acc_value


def day_08_b(list_data):
    """
    The solution code of AoC 2020 day 8 part 2 problem
    :param list_data:
    :return:
    """
    # Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp.
    # Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp).
    # What is the value of the accumulator after the program terminates?
    acc_value = 0

    # instructions_done = list()
    #
    # idx = 0
    #
    # while True:
    #     current_instr = list_data[idx]
    #
    #     if idx in instructions_done:
    #         break
    #     else:
    #         instructions_done.append(idx)
    #
    #     instr = current_instr.split(" ")
    #
    #     # Perform instruction
    #     if instr[0] == "nop":
    #         idx += 1
    #     elif instr[0] == "acc":
    #         if instr[1][0] == "+":
    #             acc_value += int(instr[1][1:])
    #         else:
    #             acc_value -= int(instr[1][1:])
    #         idx += 1
    #     elif instr[0] == "jmp":
    #         if instr[1][0] == "+":
    #             idx += int(instr[1][1:])
    #         else:
    #             idx -= int(instr[1][1:])

    return acc_value

    return list_data


def main():
    """
    Open INPUT text file, split the data into list of integers, calculate the answer and print it.
    :return:
    """
    input_data = utils_2020.open_file(sys.argv[1])

    data = input_data.split('\n')

    # list_data = [x for x in data[:-1]]
    list_data = [x for x in data]

    print('The answer for day 6 part 1 is {}'.format(day_08_a(list_data)))
    print('The answer for day 6 part 2 is {}'.format(day_08_b(list_data)))


if __name__ == '__main__':
    main()
