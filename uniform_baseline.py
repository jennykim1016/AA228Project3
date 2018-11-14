"""
This uses a random uniform baseline to evaluate the policy
"""

import random
import hyper_param

# we generate random policy for 100 times
def return_random_policy():
    random_policy = []
    num_step = hyper_param.get_policy_length()
    for step in range(num_step):
        random_policy.append(random.choice([-1, 0, 1]))
    return random_policy
