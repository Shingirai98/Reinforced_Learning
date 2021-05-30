# -----------------------------------------------------------------------------------
# |  Using Value Iteration to find the most efficient path                          |
# |  @Author : Shingirai Denver Maburutse MBRSHI002                                 |
# |  Date : 24/05/2020                                                              |
# |                                                                                 |
# -----------------------------------------------------------------------------------
import numpy as np
import argparse
import random


def find_rand(endx, endy):
    x_val = random.randint(0, endx - 1)
    y_val = random.randint(0, endy - 1)
    return x_val, y_val


def value_fxn(rec, x, y, GAMMA, x1, y1):
    v = rec[0][y][x] + (GAMMA * (rec[0][y1][x1]))
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
        print(x1, "and", y1)
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
        x2 = w - 1
        y2 = h - 1

    if args.gamma:
        g = args.gamma

    else:
        # TODO: Add a sensible learning rate of agent
        g = 0.85

    records = np.zeros((1, h, w))
    records[0][y1][x1] = 50
    records[0][y2][x2] = 100
    ditches = []
    initial_rec = [(x1, y1), (x2, y2)]

    for i in range(num):
        ditch = find_rand(w, h)
        for x in initial_rec:
            if ditch == x:
                ditch = find_rand(w, h)
            else:
                continue
        ditches.append(ditch)

    for hole in ditches:
        xh = hole[0]
        yh = hole[1]
        records[0][yh][xh] = -100

    other_rec = np.zeros((1, h, w))

    directions = {}
    for j in range(h):
        for k in range(w):
            # TODO: find the new value of the current coordinate
            other_rec[0][j][k] = 45
    # TODO: append to the records
    # np.append(records, other_rec, axis = 2)
    records = np.vstack((records, other_rec))

    print(records)

    all_states = []
    for i in range(h):
        for j in range(w):
            all_states.append((i, j))


# def value(s, gamma, S, T, R, V):
#     nextStateExpectedValue = 0
#     for nextState in getNextStates(s, S):
#         nextStateExpectedValue += T(nextState) * V(nextState)
#     return R(s) + gamma * nextStateExpectedValue


if __name__ == '__main__':
    main()
