import pandas as pd

def convert_to_csv(X,**params):
	inde_var = params.get('inde_var')

	holder = []

	for sentence in X:
		holder.append(sentence)

	df = pd.DataFrame(holder, columns = [inde_var])

	df.to_csv('./test.csv', index=False, header=True, encoding='utf-8-sig')
