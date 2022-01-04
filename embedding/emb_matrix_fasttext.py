import os
import numpy as np

def _load_embedding(**params, vocab_size = 3375+1):
    ft_dir = params.get("ft_dir")
    emb_dimension = params.get("emb_dimension")

    word_embedding = {300:{}, 200:{}, 100:{}}
    
    with open(os.path.join(directory,f'fasttext_embedding_{dimension}_pretrained.pkl'),'rb') as f:
        word_embedding[dimension] = pickle.load(f)
        
    return word_embedding[dimension]


def emb_matrix_fasttext(**params):
    # create a weight matrix for words in training docs
    embedding_matrix = np.zeros((vocab_size, emb_dimension))

    for word, index in tokenizer.word_index.items():
        #word is the key and i is the value of tokenizer.word_index.items() dictionary
        embedding_vector = word_embedding[emb_dimension].get(word)
        
        if index < vocab_size:
            if embedding_vector is not None:
                    #words not found in embedding index will be all-zeros
                    embedding_matrix[index] = embedding_vector

    return embedding_matrix

