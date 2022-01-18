import pandas as pd

def dropp_content_null(df, **params):


	df = df[df['content'].notna()]

	return df

