import numpy as np

def emb_matrix_wv(index_dict, word_vectors):

    vocab_size = len(index_dict) + 1

    embedding_weights = np.zeros((vocab_size, vocab_dim))

    for word, index in index_dict.items():
        embedding_weights[index, :] = word_vectors[word]

    return vocab_size, embedding_weights