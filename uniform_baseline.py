"""
This uses a random uniform baseline to evaluate the policy
"""

import random
import hyper_param
import numpy as np

# we generate random policy for num_step times
def return_random_policy():
    random_policy = []
    num_step = hyper_param.get_policy_length()
    for step in range(num_step):
        random_policy.append(random.choice([-1, 0, 1]))
    return random_policy

def evaluate_reward(policy, test_data, random_index):
    policy_length = len(policy)
    reward = np.dot(policy, test_data[random_index:random_index+policy_length])
    reward -= (sum(policy)*test_data[random_index+policy_length-1])
    return reward

def print_statistics_95_confidence(reward_array):
    average = sum(reward_array)/len(reward_array)
    standard_error = np.std(reward_array)/np.sqrt(len(reward_array))
    print('average:', average, "standard_error", 1.96*standard_error)

price_history = hyper_param.get_price_history()
evaluation_step = hyper_param.get_evaluation_step()

# here, we calculate the statistics for the uniform baseline ############                                     
reward_update = []
for step in range(evaluation_step):
    policy = return_random_policy()
    len_policy = len(policy)
    reward_update.append(evaluate_reward(policy, price_history, random.randint(1000, 2000)))
print_statistics_95_confidence(reward_update)
##########################################################################  
