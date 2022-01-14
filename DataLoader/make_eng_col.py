from ._scaler import _scaler

def make_eng_col(df, **params):
	eng_cols = params.get("eng_cols")

	for col in eng_cols.keys():
		df[col] = df[col].fillna(value = 0)

	coefs = []

	for col, coef in eng_cols.items():
		df[col] =  _scaler(df[col])
		df[col] = df[col] * coef

	df['engagement'] = df[eng_cols.keys()].sum(axis = 1)
	df.drop(eng_cols, axis = 1, inplace = True)

	return df