import pandas as pd

from ._scaler import _scaler

def make_eng_col(Y, **params):
	eng_cols = params.get("eng_cols")

	print('adding engagement column')

	Y = pd.DataFrame(Y, columns = list(eng_cols.keys()))

	for col, coef in eng_cols.items():
		Y[col] =  _scaler(Y[col])
		Y[col] = Y[col] * coef

	Y['engagement'] = Y[eng_cols.keys()].sum(axis = 1)
	Y.drop(eng_cols, axis = 1, inplace = True)

	return Y