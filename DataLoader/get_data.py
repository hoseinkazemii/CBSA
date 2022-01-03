import pandas as pd

def get_data(**params):
	data_directory = params.get('data_directory')
	dropped_cols = params.get('dropped_cols')

	df = pd.read_csv(data_directory)
	df.drop(dropped_cols, axis=1, inplace=True)
	# print(df.head())
	return df