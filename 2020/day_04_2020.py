"""Advent of Code 2020 - Day 4: Passport Processing"""

import sys
import re
import utils_2020


def process_list_data(list_data):
    """
    Create a list of passports
    :param list_data: input data
    :return: processed data
    """
    nu_list = list()

    tmp_str = ''
    for idx, item in enumerate(list_data):
        if item != '':
            tmp_str += ' ' + item
        else:
            nu_list.append(tmp_str)
            tmp_str = ''

        if idx == len(list_data) - 1:
            nu_list.append(tmp_str)

    return nu_list


def day_04_a(list_data):
    """
    The solution code of AoC 2020 day 4 part 1 problem
    :param list_data:
    :return:
    """
    # Birth Year
    regex_byr = re.compile(" byr:")
    # Issue Year
    regex_iyr = re.compile(" iyr:")
    # Expiration Year
    regex_eyr = re.compile(" eyr:")
    # Height
    regex_hgt = re.compile(" hgt:")
    # Hair Color
    regex_hcl = re.compile(" hcl:")
    # Eye Color
    regex_ecl = re.compile(" ecl:")
    # Passport ID
    regex_pid = re.compile(" pid:")
    # Country ID - Optional
    # regex_cid = re.compile('cid:')

    valid_passwd_sum = 0

    nu_list = process_list_data(list_data)

    valid_passports = list()

    for passwd in nu_list:
        if regex_byr.search(passwd) and regex_iyr.search(passwd) and regex_eyr.search(passwd) and \
                regex_hgt.search(passwd) and regex_hcl.search(passwd) and regex_ecl.search(passwd) \
                and regex_pid.search(passwd):
            valid_passwd_sum += 1
            valid_passports.append(passwd)

    return valid_passwd_sum, valid_passports


def day_04_b(list_data):
    """
    The solution code of AoC 2020 day 4 part 2 problem
    :param list_data:
    :return:
    """
    # Birth Year
    regex_byr = re.compile("\s?(byr:)((19[2-9][0-9])|(200[0-2]))(\s|$)")
    # Issue Year
    regex_iyr = re.compile("\s?(iyr:)(20(1[0-9]|20))(\s|$)")
    # Expiration Year
    regex_eyr = re.compile("\s?(eyr:)(20(2[0-9]|30))(\s|$)")
    # Height
    regex_hgt = re.compile("\s?(hgt:)((1([5-8][0-9]|9[0-3])cm)|((59|6[0-9]|7[0-6])in))(\s|$)")
    # Hair Color
    regex_hcl = re.compile("\s?(hcl:\#)([a-f0-9]{6})(\s|$)")
    # Eye Color
    regex_ecl = re.compile("\s?(ecl:)(amb|blu|brn|gry|grn|hzl|oth)(\s|$)")
    # Passport ID
    regex_pid = re.compile("\s?(pid:)(\d{9})(\s|$)")

    valid_passport_sum = 0

    for passport in list_data:
        if regex_byr.search(passport) and regex_iyr.search(passport) and regex_eyr.search(passport) and \
            regex_hgt.search(passport) and regex_hcl.search(passport) \
            and regex_ecl.search(passport) and regex_pid.search(passport):
            valid_passport_sum += 1

    return valid_passport_sum


def main():
    """
    Open INPUT text file, split the data into list of integers, calculate the answer and print it.
    :return:
    """
    input_data = utils_2020.open_file(sys.argv[1])

    data = input_data.split('\n')

    list_data = [x for x in data[:-1]]

    no_of_valid, valid_passports = day_04_a(list_data)

    print('The answer for day 4 part 1 is {}'.format(no_of_valid))
    print('The answer for day 4 part 2 is {}'.format(day_04_b(valid_passports)))


if __name__ == '__main__':
    main()
