"""Advent of Code 2022 - Day 2: Rock Paper Scissors"""

import sys
import utils


def day_02_a(input_data):
    """
    The solution code of AoC 2022 day 2 part 1 problem
    :return:
    """
    # Opponent: A = rock, B = paper, C = scissors
    # Me: X = rock (1 pt), Y = paper (2 pts), Z = scissors (3 pts)
    # Win = 6, Draw = 3, Lose = 0
    round_score = {'A X': 4, 'A Y': 8, 'A Z': 3,
                   'B X': 1, 'B Y': 5, 'B Z': 9,
                   'C X': 7, 'C Y': 2, 'C Z': 6}

    total_score = 0
    # Run through the strategy guide (= input_data)
    for rps_round in input_data:
        total_score += round_score[rps_round]

    return total_score


def day_02_b(input_data):
    """
    The solution code of AoC 2022 day 2 part 2 problem
    :return:
    """
    # Opponent: A = rock, B = paper, C = scissors
    # Desired Outcome: X = lose, Y = draw, Z = win
    # Chosen: rock (1 pt), paper (2 pts), scissors (3 pts)
    # Win = 6, Draw = 3, Lose = 0
    round_score = {'A X': 3, 'A Y': 4, 'A Z': 8,
                   'B X': 1, 'B Y': 5, 'B Z': 9,
                   'C X': 2, 'C Y': 6, 'C Z': 7}

    total_score = 0
    # Run through the strategy guide (= input_data)
    for rps_round in input_data:
        total_score += round_score[rps_round]

    return total_score


def main():
    """
    Open INPUT text file, split the data into list of integers, calculate the answer and print it.
    :return:
    """
    data = utils.open_file(sys.argv[1])

    list_data = data.split('\n')

    print(list_data)

    # print('The answer for day 2 part 1 is {}'.format(day_02_a(list_data)))
    print('The answer for day 2 part 2 is {}'.format(day_02_b(list_data)))


if __name__ == '__main__':
    main()
