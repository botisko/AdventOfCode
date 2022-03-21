"""Advent of Code 2017 - Day 3: Spiral Memory - Part I"""

#import sys

# Input constant
inputConst = 289326

# Constants 4 movement
CONST_U = 0
CONST_UL = 1
CONST_L = 2
CONST_LU = 3

def main():
    """Calculate the path"""
    pathSize = 0

    # Movement constant
    movementConst = -1

    # Define initial step size
    step = 268

    n = 1
    wide = 1
    dn = 0
    while n <= step:
        # step
        #print("Step:",n)
        # Dn = Odd pows
        dn = pow(2*n+1,2)
        #print("Dn:",dn)
        pathSize += 1
        wide += 2
        n += 1

    mid = wide/2+0.5
    print("Num:",dn,"Wide:",wide,"Mid:",mid,"Diff:",absdn-inputConst)

    if dn < inputConst:
        if (inputConst - dn) < wide:
            print("Dolni roh hodnota je mensi - hledame nahoru")
            movementConst = CONST_U
        else:
            print("Dolni roh hodnota je o dost mensi - hledame nahoru a doleva")
            movementConst = CONST_UL
    else:
        if (dn - inputConst) < wide:
            print("Dolni roh hodnota je vetsi - hledame vlevo")
            movementConst = CONST_L
        else:
            print("Dolni roh hodnota je o dost vetsi - hledame vlevo a nahoru")
            movementConst = CONST_LU

    # if movementConst == CONST_LU:
    #     k = 0
    #     print("jdem na while")
    #     while k < (wide*2)+((wide-1)*2)-1:
    #         print("Iter:",k,"numerko:",dn-k)
    #         k += 1

    # j = 0
    # tmp = dn
    # while tmp != inputConst:
    #     if movementConst == CONST_U:
    #         tmp += 1
    #     elif movementConst == CONST_L
    #         tmp -= 1
    #     j += 1

    print("Path size:",pathSize)

if __name__ == '__main__':
    main()
