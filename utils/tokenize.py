import jieba

def replace_all(sentence, replacements):
    
    for i, j in replacements.items():
        sentence = str(sentence).replace(i, j)
    
    return sentence


def tokenize(X, **params):
	tokenized = []

	replacements = params.get("replacements")

	for sentence in list(X):
		sentence = replace_all(sentence, replacements)

		tokenized.append(jieba.lcut(sentence, cut_all=True))

	return tokenized