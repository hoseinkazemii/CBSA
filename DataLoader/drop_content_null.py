import pandas as pd

def drop_content_null(df, **params):

	print("dropping null values from content column")

	df = df[df['content'].notna()]

	return df

