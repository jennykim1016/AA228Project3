"""
Defines the global hyper parameter for the package
"""

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
