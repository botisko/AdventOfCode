"""Advent of Code 2017 - Day 6: Memory Reallocation - Part I"""

import sys

def main():
    """Open TXT input and go through the maze"""
    stepCount = 0
    memList = list()
    # Read input file and store the values to the list
    with open(sys.argv[1]) as fp:
        for cnt, line in enumerate(fp):
            # Split the line into list
            # print("a line:",line,"a item",line[3])
            a = list(map(int, line.split(" ")))

            print("the line:",a)

            jeTam = 7 in a
            neniTam = 5 in a

            print("Sedm:",jeTam,"Pet:",neniTam)

            # Run through the list and count the checksum
            #print("Nejaka dvaitka?",a.index(20))
        var = 0
        while var < 10 :

            max = int(a[1])
            n = 0
            while n < (len(a)):
                if int(a[n]) > max:
                    max = int(a[n])
                    maxInd = n
                n += 1

            print("Index:",maxInd,"Maximalka:",max)

            # Distribute
            if maxInd == len(a)-1:
                k = 0
            else:
                k = maxInd+1

            maxTmpVal = a[maxInd]

            j = 0
            while j < maxTmpVal:
                print("Cykl:",j,"Pole:",a)
                a[k] += 1
                k += 1
                j += 1
                a[maxInd] -= 1
                if k == len(a):
                    k = 0

            print(a)

            # if a in memList == False:
            #   memList.append(a)
            #   stepCount += 1
            # # else:
            #     break
            var += 1
    print("Steps:",stepCount)

if __name__ == '__main__':
    main()
