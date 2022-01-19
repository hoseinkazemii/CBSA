import pandas as pd

def get_data(**params):
	data_directory = params.get('data_directory')
	dropped_cols = params.get('dropped_cols')

	n_samples = params.get("n_samples")

	print('loading data')

	df = pd.read_csv(data_directory)

	if not n_samples == None:
		df = df.iloc[:n_samples, :]

	df.drop(dropped_cols, axis=1, inplace=True)

	return df