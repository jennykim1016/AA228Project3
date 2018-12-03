"""
Defines the global hyper parameter for the package
"""
import numpy as np
import bisect

def get_30_t_for_eval():
    return [1777, 1669, 1099, 1352, 1467, 1534, 1978, 1130, 1671, 1364, 1488, 1203, 1666, 1227, 1458, 1040, 1974, 1487, 1461, 1714, 1415, 1888, 1023, 1833, 1468, 1811, 1945, 1983, 1176, 1698]

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
