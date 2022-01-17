from tensorflow.keras.preprocessing.sequence import pad_sequences

def padding(X, **params):
    maxlen = params.get("maxlen")

    X = pad_sequences(X, maxlen = maxlen,
        padding = 'post', truncating = 'post')

    return X