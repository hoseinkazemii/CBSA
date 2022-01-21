import pandas as pd

import time

def get_data_by_date(**params):
	data_directory = params.get("data_directory")
	n_samples = params.get("n_samples")

	df = pd.read_csv(data_directory).iloc[:n_samples, :]

	df['pubdate'] = pd.to_datetime(df['pubdate'])

	df['date'] = df['pubdate'].dt.date
	# df['time'] = df['pubdate'].dt.time

	df = df.loc[:, ['date', 'content']]

	return df

