import ast

def _replace_bad_chars(X, replacements):

	print ("Trying to replace bad chars")

	print (len(X))

	
	for i, j in replacements.items():
		print (f"{i} is being replaced")
		X = X.str.replace(i, j, regex=False)

	return X