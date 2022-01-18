import json
import numpy as np

def convert_to_json(X,**params):
	corpus_dir = params.get('corpus_dir')

	print('trying to convert json')
	
	X = np.hstack(X)
	with open('unique.json', 'w', encoding = 'utf-8-sig') as f:
		json.dump(np.unique(X).tolist(), f, ensure_ascii = False)
	# unique_words = np.unique(X)
	# strings = ''


	# for sentence in X:
	# 	string = ' '.join(sentence)
	# 	strings += string

	# with open(corpus_dir, 'w', encoding = 'utf-8-sig') as f:
	# 	json.dump(strings, f, ensure_ascii = False)