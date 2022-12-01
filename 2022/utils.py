"""Advent of Code 2022 - Utils"""


def open_file(input_file):
    """
    Open input and returns data
    :param input_file: A file with input data
    :return:
    """
    with open(input_file, "r") as f:
        return f.read()
