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

# function to return key for any value
def get_key(val, my_dict):
    for key, value in my_dict.items():
         if val == value:
             return key

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

    # discount factor
    parser.add_argument("-gamma", help="starting position", nargs=1)

    # learning rate
    parser.add_argument("-learning", help="starting position", nargs=1)

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

        start_nums = find_rand(w, h)
        x1 = start_nums[0]
        y1 = start_nums[1]

    if args.end:

        x2 = int(args.end[0])
        y2 = int(args.end[1])
    else:

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
        g = 0.85

    if args.learning:
        n = float(args.learning[0])

    else:
        n = 0.1

    if args.epochs:
        e = int(args.epochs[0])

    else:
        e = 10

    # intialize the records 3D array
    records = np.zeros((1, h, w))

    # set the environment with rewards
    records[0][y1][x1] = 0
    records[0][y2][x2] = 100
    ditches = []
    # store the cells occupied
    initial_rec = [(x1, y1), (x2, y2)]

    # store the possible actions per cell
    dxns = {}
    dxns = {
        0: (-1, 0),  # Left
        1: (1, 0),  # Right
        2: (0, 1),  # Down
        3: (0, -1),  # Up
    }

    mines = []

    # find the random coordinates for the landmines
    for i in range(num):
        ditch = find_rand(w, h)  # returns a tuple (x, y)

        while True:
            if ditch in initial_rec:
                ditch = find_rand(w, h)
                continue
            else:
                initial_rec.append(ditch)
                break

        ditches.append(ditch)

    # assign the value of -100 for landmines
    for hole in ditches:
        xh = hole[0]
        yh = hole[1]
        records[0][yh][xh] = -100
        mines.append((xh, yh))

    i = 0
    all_states = w * h
    Q_table = np.zeros((all_states, 4))


    states = {}
    i = 0

    # store the states in a dictionary
    for y in range(h):
        for x in range(w):
            states[i] = (x, y)
            i += 1





    num_ep= e
    max_moves = 100

    learning_rate = n
    discount_rate = g
    # initial exp rate
    exploration_rate = 1
    max_exploration_rate = 1
    min_exploration_rate = 0.01
    exploration_decay_rate = 0.01

    rewards = list()
    other_rec = np.zeros((1, h, w))
    # # Q-learning algorithm
    i = 0
    for episode in range(num_ep):
        for j in range(h):
            for k in range(w):

                other_rec[0][j][k] = records[i][j][k]

        current_state = get_key((x1, y1), states)
        done = False

        #     # initialize new episode params
        total_rewards = 0
        x_c = x1
        y_c = y1
        for step in range(max_moves):

            # check if exploration is better that exploitation
            if np.random.uniform(0, 1) < exploration_rate:
                # take action from dxns

                action = random.randint(0, 3)
                # Check if action is out of grid scope
                while True:

                    if x_c+dxns[action][0] < 0 or x_c+dxns[action][0] == w or y_c + dxns[action][1] == h or y_c + dxns [action][0] < 0:
                        action = random.randint(0, 3)
                        continue
                    else:
                        break
            else:
                action = np.argmax(Q_table[current_state, :])
            xt = x_c+dxns[action][0]
            yt = y_c+dxns[action][1]
            next_state = get_key((xt, yt), states)
            rew = other_rec[0][yt][xt]
            if rew == -100 or rew == 100:
                done = True

            Q_table[current_state, action] = (1 - learning_rate) * Q_table[current_state, action] + learning_rate * (rew + discount_rate * max(Q_table[next_state, :]))
            #print(Q_table[current_state, action])
            total_rewards = total_rewards + rew

            if done:
                break
            current_state = next_state

            exploration_rate = max(min_exploration_rate, np.exp(-exploration_decay_rate * e))
            rewards.append(total_rewards)

        i += 1
        records = np.vstack((records, other_rec))

    print(records)
    print("Mean reward per thousand episodes")
    print(Q_table)
    for i in range(10):
        print((i + 1) * 1000, ": mean episode reward: ", np.mean(rewards[1000 * i:1000 * (i + 1)]))
    print("\n\n")

if __name__ == '__main__':
    main()
