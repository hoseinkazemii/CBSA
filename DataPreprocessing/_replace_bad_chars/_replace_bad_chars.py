import ast

from .dicts_and_lists import replacements

def _replace_bad_chars(X):

	print ("Trying to replace bad chars")
	
	for i, j in replacements.items():
		print (f"{i} is being replaced")
		X = X.str.replace(i, j, regex=False)

	return X