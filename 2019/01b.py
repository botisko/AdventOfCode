import math


def fuel(val):
    return math.floor(int(val) / 3) - 2


def fuel_v2(val):
    required_fuel = 0

    partial_fuel = val

    while fuel(partial_fuel) >= 0:
        partial_fuel = fuel(partial_fuel)
        required_fuel += partial_fuel

    return required_fuel


def aoc_01b(filename):
    with open(filename) as f:
        content = f.readlines()

        sum_val = 0
        for val in content:
            sum_val += fuel_v2(val)

        print(sum_val)


if __name__ == '__main__':
    aoc_01b("01_input")
