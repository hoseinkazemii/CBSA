import multiprocessing as mp

from multiprocessing import Pool

from ._clean_and_tokenize_samples import _clean_and_tokenize_samples
from ._clean_and_tokenize_samples_parallel import _clean_and_tokenize_samples_parallel

from .._replace_bad_chars import _replace_bad_chars

def tokenize(X, **params):

	replacements = params.get("replacements")
	n_cores = params.get("n_cores")
	print("Trying to tokenize ...")
	
	tokenized = []

	X = _replace_bad_chars(X, replacements)

	print (X)
	raise ValueError

	if n_cores == 1:
		tokenized = _clean_and_tokenize_samples(X, replacements)

	else:
		tokenized = _clean_and_tokenize_samples_parallel(X, **params)


	print (tokenized)

	raise ValueError

	return tokenized