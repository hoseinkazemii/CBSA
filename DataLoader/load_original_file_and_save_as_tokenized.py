import pandas as pd
import json

from .get_data import get_data
from .drop_content_null import drop_content_null
from .make_eng_col import make_eng_col
from .split_data import split_data
from .segment_Y import segment_Y
from .get_X_Y_from_df import get_X_Y_from_df

from utils import tokenize
from utils import remove_space_from_all_samples
from utils import remove_stop_words

def load_original_file_and_save_as_tokenized(**params):

	df = get_data(**params)
	df = drop_content_null(df, **params)
	X, Y = get_X_Y_from_df(df, **params)
	X = tokenize(X, **params)
	X = remove_space_from_all_samples(X)
	X = remove_stop_words(X, **params)

	to_be_saved = str(X) + "|||||" + str(Y.values.tolist())

	with open('./Data/TokenizedX.json', 'w', encoding = "utf-8-sig") as f:
		json.dump(to_be_saved, f, ensure_ascii = False)

	
	print ("Tokenized file is saved.")

	