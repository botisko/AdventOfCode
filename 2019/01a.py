import math

def fuel(val):
    return math.floor(int(val)/3)-2

def aoc_01a(filename):

    with open(filename) as f:
        content = f.readlines()

        sum_val = 0
        for val in content:
            sum_val += fuel(val)

        print(sum_val)

if __name__ == '__main__':
    aoc_01a("01a_input")
