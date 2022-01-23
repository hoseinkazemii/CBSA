from DataLoader import *
from DataPreprocessing import *
from embedding import *
from MLModels import *
# from utils import *
# from BERT import *
from Polarity import *

import time

def run(**params):
	settings = {
	"n_cores": 10,
	"n_samples": None,
	'embedding_type': 'word2vec',

	"inde_var" : "content",
	"eng_cols" : {"comment_count" : 0.25, "like_count" : 0.25, 
				  "share_count" : 0.25, "view_count": 0.25},
	"de_var" : "engagement",
	"Y_segments" : 2,
	"Y_quantile" : 0.8,
	"emb_dimension" : 300,
	"maxlen" : 250, # To be subjectively optimized
	'should_plot_length': False,
	"min_word_count_wv" : 2,
	"skipgram" : 0,
	"wv_epochs" : 5,
	"window_size" : 5,

	"split_size" : 0.2,
	"k_nbrs_overs" : 5,
	"random_state" : 42,
	"pretrained_emb" : True,
	"dropout" : 0.2,
	"rec_dropout" : 0.25,
	"LSTM_cells" : [16, 32, 16],
	"lr": 0.001,
	"lr_bert": 0.00002,
	"train_epochs" : 3,
	"bert_epochs" : 10,
	"batch_size" : 2,
	"val_split" : 0.2,
	"model_verbose" : 2,
	# "checkpoint" : "hfl/chinese-bert-wwm-ext",
	"sentiment_checkpoint" : "techthiyanes/chinese_sentiment",
	"covid_checkpoint" : "yaoyinnan/bert-base-chinese-covid19",
	"bert_padding" : 512,

	}

	# One-time Run
	start = time.time()
	load_original_file_and_save_as_tokenized(**settings)
	# find_unique_words_and_save_to_json(**settings)
	# create_word2vec_embedding(**settings)
	# create_fasttext_embedding(**settings)

	print (time.time()-start)
	
	# Each time
	# index_dict, vocab_size, embedding_weights = \
	# 		load_network_info(**settings)

	# train_model_and_report(index_dict,
	# 						vocab_size,
	# 						embedding_weights,
	# 						**settings)
	# train_bert_and_report()

	#Polarity
	# df = get_data_for_polarity_analysis(**settings)
	# find_polarity_values_for_keywords(df, **settings)
	# train_ols_on_polarity_and_report(**settings)


if __name__ == '__main__':
	run()
	print("Done")
