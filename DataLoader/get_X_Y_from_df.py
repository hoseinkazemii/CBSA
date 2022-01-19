def get_X_Y_from_df(df, **params):
	inde_var = params.get('inde_var')
	de_var = list(params.get("eng_cols").keys())

	print("Getting X from data")

	X = df[inde_var]
	Y = df[de_var]

	return X, Y