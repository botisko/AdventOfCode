"""Advent of Code 2017 - Day 4: High-Entropy Passphrases - Part I"""

import sys

def main():
    """Open TXT input and count the checksum"""
    # Constants
    validPasses = 0
    linePass = True
    lineSplit = '\n'

    # Open file
    with open(sys.argv[1]) as fp:
        for cnt, line in enumerate(fp):
            # Split the line into list
            a = line.split(" ")

            # Remove \n from last string in list
            bla = a[-1]
            a[-1] = bla[:-1]

            # Compare strings in current line
            i = 0
            j = 1
            while i < len(a):
                while j < len(a):
                    # If there is a match the passphrase (line) is invalid
                    if a[i] == a[j]:
                        linePass = False
                        break
                    j += 1
                if linePass == False:
                    break
                i +=1
                j = i + 1

            # If current line is valid increment the overall passphrase count
            if linePass == True:
                validPasses += 1
            else:
                linePass = True

    print("Valid passes:",validPasses)

if __name__ == '__main__':
    main()
