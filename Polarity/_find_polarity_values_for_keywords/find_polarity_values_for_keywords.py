import json

from ._get_polarity_of_contents_for_word import _get_polarity_of_contents_for_word

def find_polarity_values_for_keywords(df, **params):
	keywords_dir = params.get("keywords_dir")

	with open(keywords_dir, 'r', encoding = 'utf-8-sig') as f:
		important_keywrods = json.load(f)

	tmp_df = df.copy()

	for word in list(important_keywrods.keys()):
		df[word] = _get_polarity_of_contents_for_word(tmp_df, word, **params)

	df = df.groupby("date").mean()

	return df