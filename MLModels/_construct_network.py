from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.layers import Flatten


def construct_network(embedding_weights, vocab_size,**params):
	pretrained_emb = params.get("pretrained_emb")
	emb_dimension = params.get("emb_dimension")
	maxlen = params.get("maxlen")
	dropout = params.get("dropout")
	rec_dropout = params.get("rec_dropout")
	LSTM_cells = params.get("LSTM_cells")

	print('constructing the deep neural network network...')

	if pretrained_emb:
		model = Sequential()

		model.add(Embedding(vocab_size, emb_dimension,
							input_length = maxlen,
                    		weights = [embedding_weights],
                    		trainable = False))
		model.add(Flatten())
		# model.add(LSTM(LSTM_cells[0],
		# 				dropout = dropout,
		# 				recurrent_dropout = rec_dropout,
		# 				return_sequences = False))
		model.add(Dense(300, activation = 'relu'))
		model.add(Dense(300, activation = 'relu'))
		model.add(Dense(1, activation = 'softmax'))
		# model.summary()

	else:
		model = Sequential()

		model.add(Embedding(vocab_size, emb_dimension, input_length = maxlen))
		# model.add(LSTM(LSTM_cells[0], dropout = dropout, recurrent_dropout = rec_dropout, return_sequences = True))
		# model.add(LSTM(LSTM_cells[1], dropout = dropout, recurrent_dropout = rec_dropout, return_sequences = True))
		# model.add(LSTM(LSTM_cells[2], dropout = dropout, recurrent_dropout = rec_dropout, return_sequences = False))
		model.add(Dense(16, activation = 'relu'))
		model.add(Dense(1, activation = 'sigmoid'))
		# model.summary()

	return model