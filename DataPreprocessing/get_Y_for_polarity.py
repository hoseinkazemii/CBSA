import pandas as pd
from DataLoader import get_hsi

def get_Y_for_polarity(**params):

	Y = get_hsi(**params)

	today_close = Y['Close']
	tomorrow_close = Y['Close'].shift(-1)

	# diff = tomorrow_close - today_close
	diff = tomorrow_close

	diff.dropna(inplace = True)

	diff.index = pd.to_datetime(diff.index)

	return diff