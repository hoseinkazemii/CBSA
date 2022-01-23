import os
import pandas as pd

from .train_ols import train_ols

from DataLoader import load_polarity_file
from DataPreprocessing import get_Y_for_polarity

from utils import Logger

def train_ols_on_polarity_and_report(**params):

	report_dir = f"./reports/OLS"
	if not os.path.exists(report_dir):
		os.mkdir(report_dir)

	logger = Logger(address = report_dir + "/Log.log")

	X = load_polarity_file()
	X = X.groupby("date").mean()
	X.index = pd.to_datetime(X.index)
	Y = get_Y_for_polarity(**params)

	df = pd.concat([X, Y], axis = 1, join = 'inner')
	X, Y = df.iloc[:, :-1], df.iloc[:, -1]

	train_ols(X, Y, logger, **params)