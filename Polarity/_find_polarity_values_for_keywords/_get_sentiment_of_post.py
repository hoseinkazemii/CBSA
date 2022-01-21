from snownlp import SnowNLP

def _get_sentiment_of_post(post, word):

	for word in words:
		if word in post:
			text = SnowNLP(post)
			return text.sentiments
	return 0.5




	sentences = text.sentences
	# print (text.sentiments)

	# imporatant_words = "".join(text.keywords(20))

	# sentiment = 0
	# if len(imporatant_words) == 0:
	# 	return sentiment
	# else:
	# 	return SnowNLP(imporatant_words).sentiments

	sentiment = 0
	if len(sentences) == 0:
		return sentiment
	else:
		for sentence in sentences:
			s = SnowNLP(sentence)
			sentiment += s.sentiments

		print (text.sentiments, sentiment/len(sentences))

		return sentiment/len(sentences)