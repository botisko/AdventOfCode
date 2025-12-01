"""Advent of Code 2025 - Day 01: Secret Entrance"""

import sys
import utils
import logging

# Set root logger to DEBUG and output to console
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def day_01_a(list_data):
    """
    The solution code of AoC 2024 day 1 part 1 problem
    :return:
    """
    no_of_zeroes = 0

    # Create a dial
    dial = list(range(0, 100))

    # Set starting index
    actual_idx = 50

    modulosto = -108 % 100
    logging.info(f"{modulosto}")

    # Walk step by step
    for instruction in list_data:
        # Dissect the instruction
        direction = instruction[0]
        if len(instruction) > 3:
            no_of_steps = int(instruction[-2:])
        elif len(instruction) < 3:
            no_of_steps = int(instruction[1])
        else:
            no_of_steps = int(instruction[1:])
        logging.debug(instruction)

        # Calculate the next index no.
        if direction == "L":
            logging.debug(f"Current index: {actual_idx}")
            actual_idx -= no_of_steps
            logging.debug(f"After rotate: {actual_idx}")
        elif direction == "R":
            logging.debug(f"Before rotate: {actual_idx}")
            actual_idx += no_of_steps
            logging.debug(f"After rotate: {actual_idx}")
        else:
            logging.error(f"Instructions unclear: {direction}")

        if abs(actual_idx) > 100:
            logging.debug(actual_idx)
            if actual_idx < 0:
                actual_idx = abs(actual_idx) % 100
                actual_idx = -actual_idx
            else:
                actual_idx %= 100

        # if abs(actual_idx) > 100:
        #     logging.debug(actual_idx)
        #     if actual_idx < 100:
        #         actual_idx %= 100
        #         # actual_idx = 200 + actual_idx
        #     elif actual_idx > 100:
        #         actual_idx %= 100
        #         # actual_idx = 200 - actual_idx
        #         actual_idx = -actual_idx

            logging.debug(f"Recalculated: {actual_idx}")

        # Check if index inbetween the bounds (-100, 100)
        # if actual_idx < -100:
        #     logging.debug(str(actual_idx)[1:])
        #     actual_idx = 100 + int(str(actual_idx)[2:])
        #     logging.debug(str(actual_idx))
        #     logging.debug(int(str(actual_idx)[2:]))
        # elif actual_idx > 100:
        #     actual_idx = 100 - int(str(actual_idx)[1:])
        #     logging.debug(int(str(actual_idx)[1:]))

        # Check the index no.
        try:
            if int(dial[actual_idx]) == 0:
                no_of_zeroes += 1
                logging.debug("Adding a zero.")
                logging.debug(no_of_zeroes)
            else:
                logging.debug(f"Current no.: {int(dial[actual_idx])}")
        except IndexError:
            logging.error(f"Wrong index {actual_idx}")
    #
    return no_of_zeroes

def day_01_b(location_ids_left, location_ids_right):
    """
    The solution code of AoC 2024 day 1 part 2 problem
    :return:
    """
    similarity_score = 0

    # for idx, _id in enumerate(location_ids_left):
    #     similarity_score += _id * location_ids_right.count(_id)

    return similarity_score


def main():
    """
    Open INPUT text file, split the data into list of integers, calculate the answer and print it.
    :return:
    """
    data = utils.open_file(sys.argv[1])

    list_data = data.split('\n')

    print('The answer for day 1 part 1 is {}'.format(day_01_a(list_data)))
    # print('The answer for day 1 part 2 is {}'.format(day_01_b(input_data)))


if __name__ == '__main__':
    main()
