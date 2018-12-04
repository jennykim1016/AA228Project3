# please fill in with the evaluation function

import hyper_param
import uniform_baseline
import pandas as pd
import sklearn
import random
from sklearn.model_selection import train_test_split
import numpy as np

def evaluate_reward(policy, test_data, random_index):
    policy_length = len(policy)
    reward = np.dot(policy, test_data[random_index:random_index+policy_length])
    reward += (sum(policy)*test_data[random_index+policy_length-1])
    return reward

def print_statistics_95_confidence(reward_array):
    average = sum(reward_array)/len(reward_array)
    standard_error = np.std(reward_array)/np.sqrt(len(reward_array))
    print('average:', average, "standard_error", 1.96*standard_error)

price_history = hyper_param.get_price_history()
training_data, test_data = sklearn.model_selection.train_test_split(price_history)
len_test_data = len(test_data)
evaluation_step = hyper_param.get_evaluation_step()

# here, we calculate the statistics for the uniform baseline ############
reward_update = []
for step in range(evaluation_step):
    policy = uniform_baseline.return_random_policy()
    len_policy = len(policy)
    reward_update.append(evaluate_reward(policy, test_data, random.randint(0, len_test_data-len_policy-1)))
print("uniform_baseline")
print_statistics_95_confidence(reward_update)
##########################################################################
