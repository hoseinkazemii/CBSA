import json
import ast

def load_tokenized_data(**params):

	with open('./Data/TokenizedX.json', 'r', encoding = "utf-8-sig") as f:
		data = json.load(f)

	X, Y = data.split("|||||")

	X = ast.literal_eval(X)
	Y = ast.literal_eval(Y)

	return X, Y
