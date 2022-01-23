from DataLoader import get_data
from DataLoader import load_tokenized_data

from DataPreprocessing import get_X_Y_from_df
from DataPreprocessing import make_eng_col
from DataPreprocessing import segment_Y

from ._parsing import parsing
from ._padding import padding
from ._train_test_split import train_test_split_
from ._oversample import oversample
from ._construct_network import construct_network
from ._train_model import train_model
from ._evaluate_classification import evaluate_classification


def train_model_and_report(index_dict,
							vocab_size,
							embedding_weights,
							**params):

	embedding_type = params.get("embedding_type")

	X, Y = load_tokenized_data(**params)

	Y = make_eng_col(Y, **params)
	Y = segment_Y(Y, **params)

	X = parsing(X, index_dict, **params)
	X = padding(X, **params)

	X_train, X_test, Y_train, Y_test = train_test_split_(X, Y, **params)
	X_train, Y_train = oversample(X_train, Y_train, **params)

	model = construct_network(embedding_weights, vocab_size, **params)
	train_model(model, X_train, Y_train, **params)
	evaluate_classification(model, X_test, Y_test,
							label = embedding_type,
							**params)