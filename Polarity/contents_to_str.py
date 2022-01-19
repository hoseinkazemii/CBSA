

def contents_to_str(X, **params):

	print("converting tokenized contents to one string for each...")

	holder = []

	for content in X:
		list_to_str = ' '.join([str(elem) for elem in content])
		holder.append(list_to_str)

	return holder