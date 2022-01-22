import pandas as pd

from .get_data import get_data

def get_data_for_polarity_analysis(**params):

	df = get_data(**params)
	df['pubdate'] = pd.to_datetime(df['pubdate'])
	df['date'] = df['pubdate'].dt.date
	df = df.loc[:, ['date', 'content']]

	return df

