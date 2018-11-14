# please fill in with the evaluation function

import hyper_param
import uniform_baseline
import pandas as pd

#evaluation_step = hyper_param.get_evaluation_steps()
#print(hyper_param.get_evaluation_steps())

def generate():
	df = pd.read_csv("ltc.csv")
	print df[['price(USD)']].iloc[1:5]