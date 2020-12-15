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

    return acc_value, instructions_done


def perform_instructions(list_data):
    """

    """
    acc_value = 0
    instructions_done = list()
    idx = 0
    while True:
        if idx == len(list_data) - 1:
            break

        current_instr = list_data[idx]

        if idx in instructions_done:
            return None
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


def day_08_b(list_data, day_08_a_instr_done):
    """
    The solution code of AoC 2020 day 8 part 2 problem
    :param list_data:
    :param day_08_a_instr_done:
    :return:
    """
    # Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp.
    # Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp).
    # What is the value of the accumulator after the program terminates?

    # List of performed instr
    loi = dict()

    for instr_idx in day_08_a_instr_done:
        loi[instr_idx] = list_data[instr_idx]

    # Loop through the list of performed instructions, find first occurence of nop/jmp and replace it in list_data.
    # Then try to run modified list_data. If it fails, move to other occurence.
    for key in loi:
        temp_instr = list_data[key]
        if "nop" in loi[key]:
            list_data[key] = loi[key].replace("nop", "jmp")
        elif "jmp" in loi[key]:
            if "0" in loi[key]:
                continue
            else:
                list_data[key] = loi[key].replace("jmp", "nop")
        else:
            continue

        if perform_instructions(list_data):
            return perform_instructions(list_data)
        else:
            list_data[key] = temp_instr


def main():
    """
    Open INPUT text file, split the data into list of integers, calculate the answer and print it.
    :return:
    """
    input_data = utils_2020.open_file(sys.argv[1])

    data = input_data.split('\n')

    # list_data = [x for x in data[:-1]]
    list_data = [x for x in data]

    day_08_a_answer, instr_done = day_08_a(list_data)

    print('The answer for day 6 part 1 is {}'.format(day_08_a_answer))
    print('The answer for day 6 part 2 is {}'.format(day_08_b(list_data, instr_done)))


if __name__ == '__main__':
    main()
