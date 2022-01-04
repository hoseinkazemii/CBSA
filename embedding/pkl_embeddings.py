# import fastText
import pickle

def pkl_embeddings(X, **params):
	emb_dimension = params.get('emb_dimension')
	chin_emb_dir = params.get('chin_emb_dir')

	word_embedding = {}
	unique_words = []

	ft = fasttext.load_model(chin_emb_dir)

	for sentence in X:
		for token in sentence:
			if token not in unique_words:
				unique_words.append(token)

			if emb_dimension == 300:
				for word in unique_words:
					word_embedding[emb_dimension][word] = ft.get_word_vector(word)

				with open(f'./embedding/my_embeddings/fasttext_embedding_{emb_dimension}_pretrained.pickle','wb') as f:
					pickle.dump(word_embedding, f) 

			elif emb_dimension == 200:
				fasttext.util.reduce_model(ft, 200)

				for word in unique_words:
					word_embedding[emb_dimension][word] = ft.get_word_vector(word)

				with open(f'./embedding/my_embeddings/fasttext_embedding_{emb_dimension}_pretrained.pickle','wb') as f:
					pickle.dump(word_embedding, f)

			elif emb_dimension == 100:
				fasttext.util.reduce_model(ft, 100)

				for word in unique_words:
					word_embedding[emb_dimension][word] = ft.get_word_vector(word)

				with open(f'./embedding/my_embeddings/fasttext_embedding_{emb_dimension}_pretrained.pickle','wb') as f:
					pickle.dump(word_embedding, f)
