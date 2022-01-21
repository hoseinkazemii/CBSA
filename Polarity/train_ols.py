import statsmodels.api as sm


def train_ols(X, Y, **params):
	print(X.shape)
	print(Y.shape)
	raise ValueError


	X = sm.add_constant(X)

	model = sm.OLS(Y, X)

	results = model.fit()

	print(results.summary())

	# return results