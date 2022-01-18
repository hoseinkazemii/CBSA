import json

def remove_stop_words(X, **params):
	stop_words_dir = params.get("stop_words_dir")

	with open(stop_words_dir, 'r', encoding = 'utf-8-sig') as f:
		stop_words = json.load(f)

	for sw in stop_words:
		for sentence in X:
			while sw in sentence:
				sentence.remove(sw)

	return X