"""Advent of Code 2017 - Day 1: Inverse Captcha - Part II"""

import sys

def advent01():
    """Open TXT input and count the captcha sum"""
    f = open(sys.argv[1],"r")

    pole = f.readline()

    totalSum = 0
    n = 0
    halfPole = int((len(pole)-1)/2)

    # Run through the input and do the countning
    while n < (halfPole):
        if int(pole[n]) == int(pole[n+halfPole]):
            totalSum = totalSum + int(pole[n]) + int(pole[n+halfPole])

        print("Index A:",n,"Actual:",pole[n],"Index N:",n+halfPole,"Next:",pole[n+halfPole],"Actual sum:",totalSum)
        n = n+1;

    print("The inverse captcha sum of the input is:",totalSum)

    f.close()

if __name__ == '__main__':
    advent01()
