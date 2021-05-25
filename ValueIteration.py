# -----------------------------------------------------------------------------------
# |  Using Value Iteration to find the most efficient path                          |
# |  @Author : Shingirai Denver Maburutse MBRSHI002                                 |
# |  Date : 24/05/2020                                                              |
# |                                                                                 |
# -----------------------------------------------------------------------------------
import numpy as np
import argparse
import random


def main():
    parser = argparse.ArgumentParser()
    # width
    parser.add_argument("width", help="display a square of a given number",
                        type=int)
    # height
    parser.add_argument("height", help="display a square of a given number",
                        type=int)
    # x1 and y1
    parser.add_argument("-start", help="starting position", nargs=2)

    # x2 and y2
    parser.add_argument("-end", help="starting position", nargs=2)

    # number of landmines
    parser.add_argument("-k", help="starting position", nargs=1)

    # learning rate
    parser.add_argument("-gamma", help="starting position", nargs=1)
    args = parser.parse_args()

    w = args.width
    h = args.height
    if args.k:
        num = args.k

    else:
        k = 3

    if args.start:
        x1 = args.start[0]
        y1 = args.start[1]
        print(x1, "and", y1)
    else:
        # TODO: Assign random numbers in the region {0;0 : w-1;h-1}
        x1 = 0
        y1 = 0
    if args.end:
        x2 = args.end[0]
        y2 = args.end[1]
    else:
        # TODO: Assign random numbers in the region {0;0 : w-1;h-1} except x1 & y1

        x2 = w - 1
        y2 = h - 1



    if args.gamma:
        g = args.gamma

    else:
        # TODO: Add a sensible learning rate of agent
        g = 0.15



def value(s, gamma, S, T, R, V):
    nextStateExpectedValue = 0
    for nextState in getNextStates(s, S):
        nextStateExpectedValue += T(nextState) * V(nextState)
    return R(s) + gamma * nextStateExpectedValue


if __name__ == '__main__':
    main()
