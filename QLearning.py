# -----------------------------------------------------------------------------------
# |  Using Q-Learning Algorithm to find the most efficient path                     |
# |  @Author : Shingirai Denver Maburutse MBRSHI002                                 |
# |  Date : 01/06/2020                                                              |
# |                                                                                 |
# -----------------------------------------------------------------------------------
import numpy as np
import argparse
import random
import matplotlib.pyplot as plt

from Animate import generateAnimat

def find_rand(endx, endy):
    x_val = random.randint(0, endx - 1)
    y_val = random.randint(0, endy - 1)
    return x_val, y_val


def value_fxn(current, GAMMA, next_v):
    v = (GAMMA * next_v)
    return v


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

    # episodes
    parser.add_argument("-epochs", help="starting position", nargs=1)

    args = parser.parse_args()

    w = args.width
    h = args.height
    num = 0
    if args.k:
        num = int(args.k[0])

    else:
        num = 3

    if args.start:
        x1 = int(args.start[0])
        y1 = int(args.start[1])
    else:
        # TODO: Assign random numbers in the region {0;0 : w-1;h-1}
        start_nums = find_rand(w, h)
        x1 = start_nums[0]
        y1 = start_nums[1]

    if args.end:

        x2 = int(args.end[0])
        y2 = int(args.end[1])
    else:
        # TODO: Assign random numbers in the region {0;0 : w-1;h-1} except x1 & y1
        end_nums = find_rand(w, h)
        while True:
            if end_nums == (x1, y1):
                end_nums = find_rand(w, h)
                continue
            else:
                break

        # x2 = random.randint(0, w-1)
        # y2 = random.randint(0, x-1)
        x2 = end_nums[0]
        y2 = end_nums[1]

    if args.gamma:
        g = float(args.gamma[0])

    else:
        # TODO: Add a sensible learning rate of agent
        g = 0.85

    if args.epochs:
        e = int(args.epochs[0])

    else:
        e = 5






if __name__ == '__main__':
    main()