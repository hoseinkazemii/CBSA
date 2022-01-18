
def _remove_space(_list,**params):

	print("cleaning text")
	
	removements = ['', ' ',]

	for obj in removements:

		while obj in _list:
			_list.remove(obj)

	return _list


def remove_spaces(X, **params):
	sentences = []

	for sentence in X:
		_remove_space(sentence)
		sentences.append(sentence)

	return sentences