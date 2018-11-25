"""
Defines the global hyper parameter for the package
"""
import numpy as np
import bisect

def get_policy_length():
    return 100

def get_evaluation_step():
    return 30

def get_train_test_split():
    return 0.7

def get_price_history():
    import pandas as pd
    df = pd.read_csv('ltc.csv')
    df[['price(USD)']] = df[['price(USD)']].fillna(method="bfill")
    return df.loc[:, ['price(USD)']].values

def get_interval_distance():
    return 0.1

def get_interval_min_slope():
    return -1.0

def get_interval_num():
    return 20

def get_interval_enum(slope):
    dist = get_interval_distance()
    minimum = get_interval_min_slope()
    num_interval = get_interval_num()
    intervals = [minimum + dist*i for i in range(num_interval)]
    return bisect.bisect_right(intervals, slope)
