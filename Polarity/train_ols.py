import statsmodels.api as sm


def train_ols(X, Y, logger, **params):

	X = sm.add_constant(X)
	model = sm.OLS(Y, X)
	results = model.fit()
	print (results.summary())
	logger.info((str(results.summary())))