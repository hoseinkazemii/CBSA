
def parsing(X, w2indx, **params):

    holder = []

    for sentence in X:
        indexed_sentence = []

        for token in sentence:
            try:
                indexed_sentence.append(w2indx[token])
            except:
                indexed_sentence.append(0)

        holder.append(indexed_sentence)

    return holder