import json
import ast
import pickle

def load_tokenized_data(**params):

	with open('./Data/TokenizedX.pkl', 'rb') as f:
		X = pickle.load(f)
		
	return X
