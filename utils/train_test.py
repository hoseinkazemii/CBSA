from sklearn.model_selection import train_test_split


def train_test(X, Y, **params):
	split_size = params.get("split_size")