import pandas as pd
import json
import pickle

from DataLoader import get_data
from ._get_X_Y_from_df import get_X_Y_from_df
from ._tokenize import tokenize
from ._text_cleaners import remove_space_from_all_samples
from ._text_cleaners import remove_stop_words


def load_original_file_and_save_as_tokenized(**params):

	df = get_data(**params)
	X, Y = get_X_Y_from_df(df, **params)
	X = tokenize(X, **params)
	X = remove_space_from_all_samples(X)
	X = remove_stop_words(X, **params)

	with open('./Data/TokenizedX.pkl', 'wb') as f:
		pickle.dump(X, f)

	print ("Tokenized file is saved.")

	