from DataLoader import *
from utils import *
from embedding import *

import json

def run(**params):
	settings = {
	"data_directory" : "./Data/analytics_challenge_dataset_ex210911.csv",
	"chin_emb_dir" : "./embedding/cc.zh.300.bin",
	"corpus_dir" : "corpus.json",
	"w2v_dir" : "./embedding/my_embeddings/w2v_model.pkl",
	"ft_dir" : "./embedding/my_embeddings/",
	"dropped_cols" : ["docid", "author*", "pubname", "region"],
	"inde_var" : "content",
	"de_var" : "like_count",
	"Y_segments" : 2,
	"Y_quantile" : 0.5,
	"replacements" : replacements,
	"emb_dimension" : 300,
	"maxlen" : 100,
	"min_word_count_wv" :1,
	"skipgram" : 0,
	"wv_epochs" : 5,
	"window_size" : 5,
	"split_size" : 0.2,
	"plot_start" : 0,
	"plot_stop" : 400,
	"plot_step" : 4,











	}

	df = get_data(**settings)
	X, Y = split_data(df, **settings)
	Y = segment_Y(Y, **settings)
	X = tokenize(X, **settings)
	X = remove_spaces(X)
	# print((count_num_words(X)))
	# convert_to_json(X, **settings)
	plot_length(X, **settings)
	

	#Option1: Word2Vec
	# index_dict, word_vectors = train_word2vec(X, **settings)
	# vocab_size, embedding_weights = emb_matrix_wv(index_dict, word_vectors, **settings)
		
	#Option2: fastText
	# vocab_size, embedding_weights = emb_matrix_fasttext(X, **settings)


	# X = parsing(X, index_dict, **settings)
	# X = padding(X, **settings)

if __name__ == '__main__':
	run()
