import numpy as np
from sklearn.metrics import classification_report

def evaluate_classification(model, X_test, Y_test, **params):

	Y_pred = model.predict(X_test)
	Y_pred = Y_pred.ravel()
	Y_pred = np.round(Y_pred).astype(int)
	print(Y_pred)
	print(Y_pred.shape)
	print('*******************************************')
	print(Y_test)
	print(Y_test.shape)
	raise ValueError

	print(classification_report(Y_test, Y_pred))