import numpy as np
import json

from DataLoader import load_tokenized_data

from ._segment_Y import segment_Y
from ._make_eng_col import make_eng_col

from utils import count_num_words
from utils import plot_length

def find_unique_words_and_save_to_json(**params):

	should_plot_length = params.get("should_plot_length")

	X = load_tokenized_data(**params)

	df = get_data(**params)
	_, Y = get_X_Y_from_df(df, **params)
	Y = make_eng_col(Y, **params)
	Y = segment_Y(Y, **params)
	# print((count_num_words(X)))
	if should_plot_length:
		plot_length(X, **params)

	print('trying to convert json')
	
	X = np.hstack(X)
	with open('./Data/unique.json', 'w', encoding = 'utf-8-sig') as f:
		json.dump(np.unique(X).tolist(), f, ensure_ascii = False)