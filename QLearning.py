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

    if args.epochs:
        e = int(args.epochs[0])

    else:
        e = 10

    records = np.zeros((1, h, w))
    records[0][y1][x1] = 0
    records[0][y2][x2] = 100
    ditches = []
    initial_rec = [(x1, y1), (x2, y2)]

    dxns = {}
    dxns = {
        0: (-1, 0),  # Left
        1: (1, 0),  # Right
        2: (0, 1),  # Down
        3: (0, -1),  # Up
    }
    mines = []
    print("A")

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

    for hole in ditches:
        xh = hole[0]
        yh = hole[1]
        records[0][yh][xh] = -100
        mines.append((xh, yh))

    i = 0
    all_states = w * h
    Q_table = np.zeros((all_states, 4))
    print(Q_table)

    
    states = {}
    i = 0
    for y in range(h):
        for x in range(w):
            states[i] = (x, y)
            i += 1
    print(states)

    # print(ditches)
    # print(mines)

    # action_space_size = env.action_space.n
    # state_space_size = env.observation_space.n
    #
    # q_table = np.zeros((state_space_size, action_space_size))
    #
    num_episodes = e
    max_steps_per_episode = 100
    #
    learning_rate = 0.1
    discount_rate = g
    #
    exploration_rate = 1
    max_exploration_rate = 1
    min_exploration_rate = 0.01
    exploration_decay_rate = 0.01
    #
    # # Q-learning algorithm
    for episode in range(num_episodes):
        #     # initialize new episode params
        #
        for step in range(max_steps_per_episode):
            # # Exploration-exploitation trade-off
            # # Take new action
            # # Update Q-table
            # # Set new state
            # # Add new reward
            #
            # # Exploration rate decay
            # # Add current episode reward to total rewards list
            # for episode in range(num_episodes):
            #  state = env.reset()
            done = False
            rewards_current_episode = 0
    #
    #     for step in range(max_steps_per_episode):
    #         # Exploration-exploitation trade-off
    #         exploration_rate_threshold = random.uniform(0, 1)
    #         if exploration_rate_threshold > exploration_rate:
    #             action = np.argmax(q_table[state, :])
    #         else:
    #             action = env.action_space.sample()
    #
    #         new_state, reward, done, info = env.step(action)
    #
    #         # Update Q-table for Q(s,a)
    #         q_table[state, action] = q_table[state, action] * (1 - learning_rate) + \
    #                                  learning_rate * (reward + discount_rate * np.max(q_table[new_state, :]))
    #
    #         state = new_state
    #         rewards_current_episode += reward
    #
    #         if done == True:
    #             break
    #
    #         # Exploration rate decay
    #         exploration_rate = min_exploration_rate + \
    #                            (max_exploration_rate - min_exploration_rate) * np.exp(-exploration_decay_rate * episode)
    #
    #         rewards_all_episodes.append(rewards_current_episode)
    #         # Calculate and print the average reward per thousand episodes
    #         rewards_per_thousand_episodes = np.split(np.array(rewards_all_episodes), num_episodes / 1000)
    #         count = 1000
    #
    #         print("********Average reward per thousand episodes********\n")
    #         for r in rewards_per_thousand_episodes:
    #             print(count, ": ", str(sum(r / 1000)))
    #             count += 1000
    #
    #         # Print updated Q-table
    #         print("\n\n********Q-table********\n")
    #         print(q_table)


if __name__ == '__main__':
    main()
