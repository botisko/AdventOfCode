"""Advent of Code 2017 - Day 2: Corruption Checksum - Part I"""

import sys

def main():
    """Open TXT input and count the checksum"""
    chckSum = 0
    with open(sys.argv[1]) as fp:
        for cnt, line in enumerate(fp):
            #print("Line {}: {}".format(cnt, line))

            # Split the line into list
            a = line.split("\t")

            # Run through the list and count the checksum
            max = int(a[1])
            min = int(a[1])
            n = 0
            while n < (len(a)):
                if int(a[n]) < min:
                    min = int(a[n])
                elif int(a[n]) > max:
                    max = int(a[n])
                n += 1

            chckSum = chckSum + (max-min)

    print("Checksum:",chckSum)
if __name__ == '__main__':
    main()
