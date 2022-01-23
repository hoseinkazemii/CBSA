import os
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

from utils import Logger

def evaluate_classification(model, x, y_true, label='CBSA', **params):

	report_dir = f"./reports/{label}"
	if not os.path.exists(report_dir):
		os.mkdir(report_dir)

	logger = Logger(address = report_dir + "/Log.log")

	y_pred = model.predict(x).reshape(-1)

	logger.info(f"--------Classification Report for - {label}----------\n" + \
	               str(classification_report(y_true, y_pred))+"\n")
	logger.info(f"--------Confusion Matrix for - {label}----------\n" + \
	               str(confusion_matrix(y_true, y_pred))+"\n")
	logger.info(f'--------Accurcay for {label}----------\n' + \
	               str(round(accuracy_score(y_true, y_pred),4)))

	print (classification_report(y_true, y_pred))
	print (f'Accuracy score for -{label}',
			round(accuracy_score(y_true, y_pred),4))
	print ("------------------------------------------------")