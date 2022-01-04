from keras.preprocessing.sequence import pad_sequences

def parse_dataset(X, w2indx, **params):
    maxlen = params.get("maxlen")

    holder = []

    for sentence in X:
        indexed_sentence = []

        for word in sentence:
            try:
                indexed_sentence.append(w2indx[word])
            except:
                indexed_sentence.append(0)

        holder.append(indexed_sentence)

    return holder
    
    X = parse_dataset(X)
    X = pad_sequences(X, maxlen = maxlen)

    return X