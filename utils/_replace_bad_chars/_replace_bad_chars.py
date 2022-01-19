import ast

def _replace_bad_chars(X, replacements):

	print (X.values.tolist())

	print (str(X.values.tolist()))

	raise ValueError ("Inside _replace_bad_chars")
	
	for i, j in replacements.items():
		X = str(X.values).replace(i, j)

	X = ast.literal_eval(X)

	return X