import jieba

def _replace_all(sentence, replacements):
    
    for i, j in replacements.items():
        sentence = str(sentence).replace(i, j)
    
    return sentence


def tokenizerr(X, **params):
	replacements = params.get("replacements")

	print("tokenizing")

	tokenized = []

	for idx, sentence in enumerate(X[:250000]):
		sentence = _replace_all(sentence, replacements)

		tokenized.append(jieba.lcut(sentence, cut_all=True))
		print(idx)

	tokenized_2 = []

	for idx, sentence in enumerate(X[250000:]):
		sentence = _replace_all(sentence, replacements)

		tokenized_2.append(jieba.lcut(sentence, cut_all=True))
		print(idx)

	tokenized.extend(tokenized_2)

	return tokenized