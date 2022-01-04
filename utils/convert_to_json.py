import json

def convert_to_json(X,**params):
	corpus_dir = params.get('corpus_dir')
	
	strings = ''

	for sentence in X:
		string = ' '.join(sentence)
		strings += string

	with open(corpus_dir, 'w', encoding='utf-8-sig') as f:
		json.dump(strings, f, ensure_ascii=False)