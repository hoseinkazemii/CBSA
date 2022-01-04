from gensim.corpora.dictionary import Dictionary
from keras.preprocessing.sequence import pad_sequences


def emb_dict(X, model, **params):
    maxlen = params.get("maxlen")

    if model is not None:

        gensim_dict = Dictionary()
        gensim_dict.doc2bow(model.vocab.keys(), allow_update=True)
        w2indx = {v: k+1 for k, v in gensim_dict.items()}
        w2vec = {word: model[word] for word in w2indx.keys()}

        def parse_dataset(X):

            data=[]
            for sentence in X:
                new_txt = []
                for word in sentence:
                    try:
                        new_txt.append(w2indx[word])
                    except:
                        new_txt.append(0)
                data.append(new_txt)

            return data
            
        X = parse_dataset(X)
        X = pad_sequences(X, maxlen = maxlen)
        
        return w2indx, w2vec, X

    else:
        print('model is not trained yet')
