import json

from ._get_polarity_of_contents_for_word import _get_polarity_of_contents_for_word

def find_polarity_values_for_keywords(df, **params):

	# keywords_dir = params.get("keywords_dir")

	# with open(keywords_dir, 'r', encoding = 'utf-8-sig') as f:
	# 	keywords = json.load(f)

	important_keywrods = [['疫情'],
						'檢疫', "內地"]

	tmp_df = df.copy()

	for word in important_keywrods:
		df[word] = _get_polarity_of_contents_for_word(tmp_df, word, **params)

	df = df.groupby("date").mean()

	return df