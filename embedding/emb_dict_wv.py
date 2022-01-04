from gensim.corpora.dictionary import Dictionary

def emb_dict_wv(model, **params):

    if model is not None:

        gensim_dict = Dictionary()
        gensim_dict.doc2bow(model.wv.key_to_index.keys(), allow_update=True)

        w2indx = {v: k+1 for k, v in gensim_dict.items()}
        w2vec = {word: model.wv.get_vector(word) for word in w2indx.keys()}
        
        return w2indx, w2vec

    else:
        print('model is not trained yet')
