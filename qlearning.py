import pandas as pd
import hyper_param
import numpy as np
import random
import bisect

def get_interval_enum(slope):
    dist = hyper_param.get_interval_distance()
    minimum = hyper_param.get_interval_min_slope()
    num_interval = hyper_param.get_interval_num()
    intervals = [minimum + dist*i for i in range(num_interval)]
    return bisect.bisect_right(intervals, slope)

def generate_simulation(t, a, s, price):
#    print("action", a)
#    print("time", t)
    x = [t+i for i in range(10)]
    y = price[t-10:t]
    slope, intercept = np.polyfit(x, y, 1)
    reward = 0
    if s[1] <= -50 or s[1] >= 50:
        return (0, (get_interval_enum(slope[0]), 0))
    else:
        if a == -1:
            reward = 0-price[t][0]
        elif a == 1:
            reward = price[t][0]
        elif a == 0:
            reward = 0
        else:
            #throw expection
            print("Invalid Argument")
    interval_group = get_interval_enum(slope[0])
    return (reward, (interval_group, s[1]+1))

def generate_Q_learning_policy(Q, t, price):
    policy = []
    cur_num_coins = 0
    for time in range(t, t+100):
        x = [t+i for i in range(10)]
        y = price[t-10:t]
        slope, intercept = np.polyfit(x, y, 1)
        interval_group = get_interval_enum(slope[0])
        if (interval_group, cur_num_coins) in Q: 
            Q_value = Q[(interval_group, cur_num_coins)]
        action = max(Q_value, key=Q_value.get)

### beginning of Q learning
Q = {}
alpha = 1.0
price = hyper_param.get_price_history()
num_iter = 1000
gamma = 0.9

# dummy slope interval, 0 coin
s = (0, 0)
for trial in range(100):
    t = 1000 # backfilled so not reliable
    for i in range(num_iter):
        cur_Q = 0
        Q_value = 0
        if s in Q:
            Q_value = Q[s]
            prob = random.uniform(0, 1)
            if prob <= 0.8:
                action = max(Q_value, key=Q_value.get)
                cur_Q = Q_value[action]
            else:
                action = random.choice([-1, 0, 1])
                if action in Q_value:
                    cur_Q = Q_value[action]
        else:
            action = random.choice([-1, 0, 1])
### state: (slope interval, number of coins holding)
        r, sp = generate_simulation(t, action, s, price)
#        print('r', r, 'sp', sp)
        new_Q = 0
        if sp in Q:
            new_Q_action = max(Q[sp], key=Q[sp].get)
            new_Q = Q[sp][new_Q_action]
        t += 1
        if s in Q:
            Q[s][action] = (cur_Q + alpha * (r + gamma * new_Q - cur_Q))
        else:
            Q[s] = {action: (cur_Q + alpha * (r + gamma * new_Q - cur_Q))}
        s = sp
    
