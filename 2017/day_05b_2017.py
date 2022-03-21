"""Advent of Code 2017 - Day 5: A Maze of Twisty Trampolines, All Alike - Part II"""

import sys

def main():
    """Open TXT input and go through the maze"""
    maze = list()
    # Read input file and store the values to the list
    with open(sys.argv[1]) as fp:
        for cnt, line in enumerate(fp):
            # Add current line to the list
            maze.append(int(line))

    stepCount = 0

    ind = 0
    while ind < len(maze):
        # Count the next index
        nextInd = ind + maze[ind]
        # Modify current value
        if maze[ind] >= 3:
            maze[ind] -= 1
        else:
            maze[ind] += 1
        # Assign next index
        ind = nextInd
        # Increment the count of steps
        stepCount += 1

    print("Steps:",stepCount)

if __name__ == '__main__':
    main()
