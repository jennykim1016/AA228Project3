"""
Defines the global hyper parameter for the package
"""
import numpy as np
import bisect

def get_30_t_for_eval():
    return [1497,1638,1532,1734,1165,1471,1077,1764,1700,1111,1829,1570,1154,1411,1561,1292,1112,1015,1188,1870,1718,1695,1120,1200,1042,1591,1301,1855,1092,1087]

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
