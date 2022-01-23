import pandas as pd

from ._drop_content_null import _drop_content_null

def get_data(**params):
	eng_cols = params.get("eng_cols")
	n_samples = params.get("n_samples")

	print('loading data')

	df = pd.read_csv("./Data/analytics_challenge_dataset_ex210911.csv")

	if not n_samples == None:
		df = df.iloc[:n_samples, :]

	for col in eng_cols.keys():
		df[col] = df[col].fillna(value = 0)

	df.drop(columns = ["docid", "author*", "pubname", "region"],
			inplace=True)
	df = _drop_content_null(df)

	return df