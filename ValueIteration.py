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
        g = float(args.gamma[0])

    else:
        # TODO: Add a sensible learning rate of agent
        g = 0.85

    records = np.zeros((1, h, w))
    records[0][y1][x1] = 0
    records[0][y2][x2] = 100
    ditches = []
    initial_rec = [(x1, y1), (x2, y2)]

    dxns = {}
    dxns = {
        0: (-1, 0),  # Left
        1: (1, 0),   # Right
        2: (0, 1),  # Down
        3: (0, -1),  # Up
    }

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
    i = 0
    while True:
        for j in range(h):
            for k in range(w):
                # TODO: find the new value of the current coordinate
                other_rec[0][j][k] = records[i][j][k]
        # TODO: append to the records

        # update iteration record based on new values
        for j in range(h):
            for k in range(w):
                if other_rec[0][j][k] == -100 or other_rec[0][j][k] == 100:
                    continue
                # old_V = other_rec[0][j][k]
                new_V = 0
                for d in dxns:
                    try:
                        if j+(dxns[d])[1] < 0 or k+(dxns[d])[0] <0 or j+(dxns[d])[1] == h or k+(dxns[d])[0] == w:
                            continue
                        next_v = records[i][j+(dxns[d])[1]][k+(dxns[d])[0]]

                    except IndexError:
                        continue

                    v = value_fxn(records[i][j][k], g, next_v)

                    if v > new_V:
                        new_V = v

                other_rec[0][j][k] = new_V

        comparison = records[i] == other_rec[0]
        equ = comparison.all()
        if equ and i >0:
            break
        records = np.vstack((records, other_rec))

        i+=1

    print(records)



# def value(s, gamma, S, T, R, V):
#     nextStateExpectedValue = 0
#     for nextState in getNextStates(s, S):
#         nextStateExpectedValue += T(nextState) * V(nextState)
#     return R(s) + gamma * nextStateExpectedValue


if __name__ == '__main__':
    main()
