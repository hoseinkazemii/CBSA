import time

from ._get_sentiment_of_post import _get_sentiment_of_post

def _get_polarity_of_contents_for_word_process(df, word, results_queue):

	sentiments = []
	for post in df['content']:
		sentiments.append(_get_sentiment_of_post(post))

	df['sentiments'] = sentiments

	results_queue.put(df)



