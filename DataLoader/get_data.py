import pandas as pd

from ._drop_content_null import _drop_content_null

def get_data(**params):
	data_directory = params.get('data_directory')
	dropped_cols = params.get('dropped_cols')
	eng_cols = params.get("eng_cols")

	n_samples = params.get("n_samples")

	print('loading data')

	df = pd.read_csv(data_directory)

	if not n_samples == None:
		df = df.iloc[:n_samples, :]

	for col in eng_cols.keys():
		df[col] = df[col].fillna(value = 0)

	df.drop(dropped_cols, axis=1, inplace=True)
	df = _drop_content_null(df)

	return df