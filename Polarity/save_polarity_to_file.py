

def save_polarity_to_file(df, **params):
	polarity_dir = params.get("polarity_dir")

	df.to_csv(polarity_dir)