# # import json

# # with open('corpus.json', 'r') as f:
# # 	a = f.read()

# # print(a)

# # import gensim

# from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
# import pandas as pd

# df = pd.read_csv('./Data/analytics_challenge_dataset_ex210911.csv')

# checkpoint = "hfl/chinese-bert-wwm-ext"

# tokenizer = AutoTokenizer.from_pretrained(checkpoint)
# model = TFAutoModelForSequenceClassification.from_pretrained(checkpoint)

# for sentence in df['content']:
# 	sentence = str(sentence)
# 	model_inputs = tokenizer(sentence)
# 	# tokens = tokenizer.tokenize(sentence)
# 	output = model(model_inputs)
# 	print(output)


import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import transformers
from transformers import AutoModel, BertTokenizerFast



from DataLoader import *
from MLModels import *
from BERT import *
from utils import *
from embedding import *


# def run(**params):
# 	settings = {
# 	"data_directory" : "./Data/analytics_challenge_dataset_ex210911.csv",
# 	"chin_emb_dir" : "./embedding/cc.zh.300.bin",
# 	"corpus_dir" : "corpus.json",
# 	"w2v_dir" : "./embedding/my_embeddings/w2v_model.pkl",
# 	"ft_dir" : "./embedding/my_embeddings/",
# 	"dropped_cols" : ["docid", "author*", "pubname", "region"],
# 	"inde_var" : "content",
# 	"eng_cols" : {"comment_count" : 0.25, "like_count" : 0.25, 
# 				  "share_count" : 0.25, "view_count": 0.25},
# 	"de_var" : "engagement",
# 	"Y_segments" : 2,
# 	"Y_quantile" : 0.5,
# 	"replacements" : replacements,
# 	"emb_dimension" : 300,
# 	"maxlen" : 100,
# 	"min_word_count_wv" :1,
# 	"skipgram" : 0,
# 	"wv_epochs" : 5,
# 	"window_size" : 5,
# 	"split_size" : 0.2,
# 	"k_nbrs_overs" : 5,
# 	"plot_start" : 0,
# 	"plot_stop" : 400,
# 	"plot_step" : 4,
# 	"random_state" : 42,
# 	"pretrained_emb" : True,
# 	"dropout" : 0.2,
# 	"rec_dropout" : 0.25,
# 	"LSTM_cells" : [16, 32, 16],
# 	"lr": 0.001,
# 	"lr_bert": 0.00002,
# 	"train_epochs" : 10,
# 	"bert_epochs" : 10,
# 	"batch_size" : 2,
# 	"val_split" : 0.2,
# 	"model_verbose" : 2,
# 	"checkpoint" : "hfl/chinese-bert-wwm-ext",
# 	"bert_padding" : 512,











# 	}

# 	#option3: BERT
# 	df = get_data(**settings)
# 	df = make_eng_col(df, **settings)
# 	X, Y = split_data(df, **settings)
# 	Y = segment_Y(Y, **settings)
# 	X = clean_text(X, **settings)
# 	# X_train = remove_spaces(X_train)
# 	X_train, X_test, Y_train, Y_test = train_test(X, Y, **settings)
# 	X_val, X_test, Y_val, Y_test = split_val_test(X_test, Y_test, **settings)
# 	X_train = tokenize_bert(X_train, **settings)
# 	X_val = tokenize_bert(X_val, **settings)
# 	X_test = tokenize_bert(X_test, **settings)
# 	X_train_seq, X_train_mask, Y_train = sequence_to_tensor(X_train, Y_train, **settings)
# 	X_val_seq, X_val_mask, Y_val = sequence_to_tensor(X_val, Y_val, **settings)
# 	X_test_seq, X_test_mask, Y_test = sequence_to_tensor(X_test, Y_test, **settings)
# 	train_dataloader, val_dataloader = data_loader(X_train_seq, X_train_mask, Y_train,
# 			    								   X_val_seq, X_val_mask, Y_val, **settings)
# 	bert = initialize_bert(X_train_seq, X_train_mask, **settings)
# 	model, optimizer, weights, cross_entropy, device = fine_tune(bert, Y_train, **settings)
# 	start_training(model, train_dataloader, val_dataloader, cross_entropy, optimizer, **settings)
# 	predict_test(model, Y_test, **params)



# if __name__ == '__main__':
# 	run()



list_1 = [1,2,3]
list_2 = [4,5]

list_1.extend(list_2)
print(list_1)





