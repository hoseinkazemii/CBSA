import pandas as pd


def load_polarity(**params):
	polarity_dir = params.get("polarity_dir")

	df = pd.read_csv(polarity_dir)

	df.drop(['date'], axis = 1, inplace = True)

	return df