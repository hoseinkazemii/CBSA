from .emb_dict import emb_dict

import gensim
import multiprocessing as mp

def word2vec(X, **params):
	emb_dimension = params.get("emb_dimension")
	min_word_count_wv = params.get("min_word_count_wv")
	window_size = params.get("window_size") 
	skipgram = params.get("skipgram")
	wv_epochs = params.get("wv_epochs")
	w2v_dir = params.get("w2v_dir")
    maxlen = params.get("maxlen")

	workers = mp.cpu_count() - 2

	model = gensim.models.word2vec.Word2Vec(sentences = X,
								   			vector_size = emb_dimension,
								   			window = window_size,
								   			min_count = min_word_count_wv,
								   			sg = skipgram,
								   			epochs = wv_epochs,
								   			)

	model.build_vocab(X)
	model.train(X)
	model.save(w2v_dir)

    index_dict, word_vectors,combined = emb_dict(X = X, model = model, **self.__dict__)
    return   index_dict, word_vectors, X