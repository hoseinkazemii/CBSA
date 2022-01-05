import os
import numpy as np
import pickle
from tensorflow.keras.preprocessing.text import Tokenizer

def _load_embedding(**params):
    ft_dir = params.get("ft_dir")
    emb_dimension = params.get("emb_dimension")

    word_embedding = {300:{}, 200:{}, 100:{}}

    with open(os.path.join(ft_dir,f'fasttext_embedding_{emb_dimension}_pretrained.pkl'),'rb') as f:
        word_embedding[emb_dimension] = pickle.load(f)
        
    return word_embedding[emb_dimension]


def emb_matrix_fasttext(X, vocab_size = 3375+1, **params):
    emb_dimension = params.get("emb_dimension")

    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(X)
    w2indx = tokenizer.word_index
    # create a weight matrix for words in training docs
    embedding_matrix = np.zeros((vocab_size, emb_dimension))

    word_embedding = _load_embedding(**params)

    for word, index in w2indx.items():
        #word is the key and i is the value of tokenizer.word_index.items() dictionary
        embedding_vector = word_embedding[emb_dimension].get(word)
        
        if index < vocab_size:
            if embedding_vector is not None:
                    #words not found in embedding index will be all-zeros
                    embedding_matrix[index] = embedding_vector

    return vocab_size, w2indx, embedding_matrix

