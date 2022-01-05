from sklearn.model_selection import train_test_split


def split(X, **params):
	split_size = params.get("split_size")