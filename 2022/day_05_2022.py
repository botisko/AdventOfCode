"""Advent of Code 2022 - Day 5: Supply Stacks"""

import sys
import utils


def day_05_a(inverted_matrix, instructions):
    """
    The solution code of AoC 2022 day 5 part 1 problem
    :return:
    """
    for move in instructions:
        move_list = move.split(" ")
        # Get the instructions
        no_of_crates = int(move_list[1])
        from_stack = int(move_list[3]) - 1
        to_stack = int(move_list[5]) - 1

        # Pop the crates one-by-one and put them into the right column
        for _ in range(0, no_of_crates):
            inverted_matrix[to_stack].append(inverted_matrix[from_stack].pop())

    message = str()

    # Print the result message
    for col in inverted_matrix:
        message += col[-1]

    return message


def day_05_b(inverted_matrix, instructions):
    """
    The solution code of AoC 2022 day 5 part 2 problem
    :return:
    """
    for move in instructions:
        move_list = move.split(" ")
        # Get the instructions
        no_of_crates = int(move_list[1])
        from_stack = int(move_list[3]) - 1
        to_stack = int(move_list[5]) - 1

        # Store the moved crates into list, reverse it and then put it into right column
        moved_crates = list()

        for _ in range(0, no_of_crates):
            moved_crates.append(inverted_matrix[from_stack].pop())

        moved_crates.reverse()
        inverted_matrix[to_stack] += moved_crates

    message = str()

    # Print the result message
    for col in inverted_matrix:
        message += col[-1]

    return message


def main():
    """
    Open INPUT text file, split the data into list of integers, calculate the answer and print it.
    :return:
    """
    data = utils.open_file(sys.argv[1])

    list_data = data.split('\n')

    crate_matrix = list()
    instructions = list()

    for i, crates in enumerate(list_data):
        if crates == '':
            continue
        elif crates[0].isalpha():
            # Store instructions in a different list
            instructions.append(crates)
        else:
            # Replace multiple (4) spaces with one
            crate = crates.replace(4 * " ", " ")
            # Append a row to the matrix
            crate_matrix.append(crate.split(" "))

    # Get the row length
    row_length = crate_matrix[-1][-1]
    # Remove the idx row
    crate_matrix = crate_matrix[:-1][:]
    # Allocate inverted matrix
    inverted_matrix = [[None] * 1 for _ in range(int(row_length))]

    # Invert the crate matrix
    for i, row in enumerate(crate_matrix):
        for j, crate in enumerate(row):
            if crate != '':
                inverted_matrix[j].append(crate)

    # Remove None items and reverse the column order
    for i, column in enumerate(inverted_matrix):
        inverted_matrix[i].pop(0)
        inverted_matrix[i].reverse()

    # print('The answer for day 5 part 1 is {}'.format(day_05_a(inverted_matrix, instructions)))
    print('The answer for day 5 part 2 is {}'.format(day_05_b(inverted_matrix, instructions)))


if __name__ == '__main__':
    main()
