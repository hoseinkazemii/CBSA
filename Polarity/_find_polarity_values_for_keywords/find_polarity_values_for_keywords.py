import json

from ._get_polarity_of_contents_for_word import _get_polarity_of_contents_for_word

def find_polarity_values_for_keywords(df, **params):

	# keywords_dir = params.get("keywords_dir")

	# with open(keywords_dir, 'r', encoding = 'utf-8-sig') as f:
	# 	keywords = json.load(f)

	important_keywrods = ['冠状病毒病', '银行', '中国']

	for word in important_keywrods:
		df[word] = _get_polarity_of_contents_for_word(df, word, **params)

	df = _average_polarities_by_date(df)

	df.drop(columns = ["A", "B"], inplace = True)

	return df