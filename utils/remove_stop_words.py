import time
import json

def remove_stop_words(X, **params):
	"""
	X: list of list
	"""

	stop_words_dir = params.get("stop_words_dir")

	print("removing stop words")

	with open(stop_words_dir, 'r', encoding = 'utf-8-sig') as f:
		stop_words = json.load(f)	

	for sw in stop_words:
		for sentence in X:
			try:
				while True:
					sentence.remove(sw)
			except ValueError:
				pass

	return X