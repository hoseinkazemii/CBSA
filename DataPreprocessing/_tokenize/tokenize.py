import multiprocessing as mp

from multiprocessing import Pool

from ._tokenize_samples import _tokenize_samples
from ._tokenize_samples_parallel import _tokenize_samples_parallel

from .._replace_bad_chars import _replace_bad_chars

def tokenize(X, **params):

	n_cores = params.get("n_cores")
	print("Trying to tokenize ...")
	
	tokenized = []

	X = _replace_bad_chars(X)

	if n_cores == 1:
		tokenized = _tokenize_samples(X)

	else:
		tokenized = _tokenize_samples_parallel(X, **params)

	return tokenized