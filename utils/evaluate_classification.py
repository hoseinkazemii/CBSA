import numpy as np
from sklearn.metrics import classification_report

def evaluate_classification(model, X_test, Y_test, **params):

	Y_pred = model.predict(X_test)
	Y_pred = np.round(Y_pred).astype(int)

	print(classification_report(Y_test, Y_pred))