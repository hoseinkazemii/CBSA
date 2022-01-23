import json

def load_unique_words(**params):

	with open("./Data/unique.json", 'r', encoding = 'utf-8-sig') as f:
		unique_words = json.load(f)

	return unique_words