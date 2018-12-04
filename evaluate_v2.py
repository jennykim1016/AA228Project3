from __future__ import print_function
import numpy as np
import random
import hyper_param as hp
import qlearning
import pickle
import evaluate
import uniform_baseline

def evaluate_reward(policy, test_data, random_index):
    policy_length = len(policy)
    reward = np.dot(policy, test_data[random_index:random_index+policy_length])
    reward -= (sum(policy)*test_data[random_index+policy_length-1])
    return reward

def upper_bound_of_maximum_gain(time_step, prices, horizon):
    #all_prices_in_100_time_step = np.array(prices[time_step: time_step + horizon])
    all_prices_in_100_time_step = np.array(prices[time_step: time_step + horizon])
    closing_price = all_prices_in_100_time_step[-1]
    diff = all_prices_in_100_time_step - closing_price
    return np.sum(np.absolute(diff))  

def plotAll(t_array, upper_bound_array, reward_array):
    import matplotlib.pyplot as plt
    plt.figure()
    plt.plot(t_array, upper_bound_array, 'bx')
    plt.plot(t_array, reward_array, 'go')
    plt.show()
    
def plotAll2(t_array, upper_bound_array, reward_array, method, title):
    import pylab
    pylab.plot(t_array, upper_bound_array, 'b^', label='upper bound of utility')
    pylab.plot(t_array, reward_array, 'r^', label='utility of our policy')
    pylab.plot(t_array, -np.array(upper_bound_array), 'g^', label='lower bound of utility')
    pylab.legend(loc='upper right')
    pylab.xlabel('t')
    pylab.ylabel('Utility')
    pylab.title(method)
    pylab.savefig(title)

print("here")
    
prices = hp.get_price_history().squeeze()
t_array = []
upper_bound_array = []
reward_array = []
random_number = hp.get_30_t_for_eval()
print(random_number)

for i in range(hp.get_evaluation_step()):
    random_time = random_number[i]
    policy_length = hp.get_policy_length()
    #policy = generate_NN_1_step_policy(random_time, prices, policy_length)
    #qlearning_policy = qlearning.generate_Q_learning_policy(random_time, policy_length)
    policy = uniform_baseline.return_random_policy()
    t_array.append(random_time)
    upper_bound_array.append(upper_bound_of_maximum_gain(random_time, prices, hp.get_policy_length()))
    reward_array.append(evaluate.evaluate_reward(policy, prices, random_time))
    #reward_array.append(evaluate.evaluate_reward(qlearning_policy, prices, random_time))
    
plotAll2(t_array, upper_bound_array, reward_array, method='baseline', title="baseline")

## we calculate the percentage gain
## change everything to the upper bound
diff_lowerbound = -(np.array(reward_array) - np.array(upper_bound_array))
range_ = 2*np.array(upper_bound_array)
percent_gain = diff_lowerbound / range_
print("percentage gain:", np.mean(percent_gain)-0.5, "std: ",np.std(percent_gain))
print("average reward", np.mean(reward_array))

for i in range(hp.get_evaluation_step()):
    random_time = random_number[i]
    policy_length = hp.get_policy_length()
    #policy = generate_NN_1_step_policy(random_time, prices, policy_length)                                                                                           
    qlearning_policy = qlearning.generate_Q_learning_policy(random_time, policy_length)                                                                              
    policy = uniform_baseline.return_random_policy()
    t_array.append(random_time)
    upper_bound_array.append(upper_bound_of_maximum_gain(random_time, prices, hp.get_policy_length()))
    #reward_array.append(evaluate.evaluate_reward(policy, prices, random_time))
    reward_array.append(evaluate.evaluate_reward(qlearning_policy, prices, random_time))                                                                             

plotAll2(t_array, upper_bound_array, reward_array, method='baseline', title="baseline")

## we calculate the percentage gain                                                                                                                                   
## change everything to the upper bound                                                                                                                               
diff_lowerbound = -(np.array(reward_array) - np.array(upper_bound_array))
range_ = 2*np.array(upper_bound_array)
percent_gain = diff_lowerbound / range_
print("percentage gain:", np.mean(percent_gain)-0.5, "std of percent gain:", np.std(percent_gain))
print("average reward", np.mean(reward_array))
