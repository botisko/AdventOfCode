"""Advent of Code 2017 - Day 2: Corruption Checksum - Part II"""

import sys

def main():
    """Open TXT input and count the checksum"""
    chckSum = 0
    with open(sys.argv[1]) as fp:
        for cnt, line in enumerate(fp):
            #print("Line {}: {}".format(cnt, line))

            # Split the line into list
            data = list(map(int, line.split("\t")))

            # Descending sort
            data.sort(reverse=True)

            # Run through the rows and calculate line checksum
            i = 0
            j = 1
            while i < len(data):
                while j < (len(data)-i):
                    if (data[i] % data[j+i]) == 0:
                        chckSum += data[i] / data[j+i]
                    j += 1;
                j = 1
                i += 1;

        # Print the checksum of all lines
        print("Total chckSum:",chckSum)

if __name__ == '__main__':
    main()
