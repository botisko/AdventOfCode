import math

def fuel_v2(val, sum_val):
    print(val)
    print(sum_val)
    if math.floor(int(val)/3)-2 <= 0:
        return sum_val
    else:
        sum_val += val
        fuel_v2(math.floor(int(val)/3)-2, sum_val)

def aoc_01b(filename):

    # print(fuel_v2(14))
    print(fuel_v2(1969, 0))


    # with open(filename) as f:
    #     content = f.readlines()
    #
    #     sum_val = 0
    #     for val in content:
    #         sum_val += fuel(val)
    #
    #     print(sum_val)

if __name__ == '__main__':
    aoc_01b("01_input")
