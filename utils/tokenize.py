import jieba

def _replace_all(sentence, replacements):
    
    for i, j in replacements.items():
        sentence = str(sentence).replace(i, j)
    
    return sentence


def tokenize(X, replacements):

	print("tokenizing")
	
	tokenized = []

	for idx, sentence in enumerate(X):
		sentence = _replace_all(sentence, replacements)

		tokenized.append(jieba.lcut(sentence, cut_all=True))
		print(idx)


	return tokenized