import jieba

from .._replace_bad_chars import _replace_bad_chars

def _clean_and_tokenize_samples(X,
								replacements,
								batch_number = None,
								q_out = None):

	tokenized = []
	for idx, sentence in enumerate(X):

		# sentence = _replace_bad_chars(sentence, replacements)
		tokenized = jieba.lcut(sentence, cut_all=True)

	if q_out == None:
		return tokenized
	else:
		q_out.put((batch_number, tokenized))

