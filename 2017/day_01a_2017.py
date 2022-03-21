"""Advent of Code 2017 - Day 1: Inverse Captcha - Part I"""

import sys

def advent01():
    """Open TXT input and count the captcha sum"""
    f = open(sys.argv[1],"r")

    pole = f.readline()

    totalSum = 0
    n = 0

    # Run through the input and do the countning
    while n < (len(pole)-2):
        if int(pole[n]) == int(pole[n+1]):
            totalSum = totalSum + int(pole[n])

        # print("Index:",n,"Actual:",pole[n],"Next:",pole[n+1],"Actual sum:",totalSum)
        n = n+1;

    # Compare the 1st and last ("circle buffer")
    if int(pole[0]) == int(pole[-2]):
        totalSum = totalSum + int(pole[0])

    print("The inverse captcha sum of the input is:",totalSum)

    f.close()

if __name__ == '__main__':
    advent01()
