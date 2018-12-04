"""
Defines the global hyper parameter for the package
"""
import numpy as np
import bisect

def get_30_t_for_eval():
    return [1205, 1663, 1441, 1329, 1537, 1289, 1242, 1600, 1501, 1101, 1516, 1296, 1695, 1451, 1873, 1095, 1631, 1243, 1058, 1455, 1535, 1575, 1233, 1702, 1571, 1150, 1561, 1518, 1613, 1323]

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
