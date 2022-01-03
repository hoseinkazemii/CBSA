def split_data(df, **params):
	inde_var = params.get('inde_var')
	de_var = params.get('de_var')

	X = df[inde_var]
	Y = df[de_var]

	return X, Y