"""
Author: Lee Taylor
"""
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
import numpy as np
import pickle
import string
import gensim
import os


def train_model(corpus_):
    """

    :param corpus_:
    :return:
    """
    # Train the word2vec model on the corpus
    model_ = gensim.models.Word2Vec(corpus_, vector_size=300)
    return model_


def save_model(model_, file_path):
    """

    :param model_:
    :param file_path:
    """
    # Save the weights of the trained model
    model_.save(file_path)


def read_words_from_file(file_path, encoding='utf-8-sig',
                         rtype='set'):
    """

    :param rtype:
    :param encoding:
    :param file_path:
    :return:
    """
    with open(file_path, 'r', encoding=encoding) as f:
        if rtype == 'set':
            words = set(f.read().splitlines())
        elif rtype == 'list':
            words = f.read().splitlines()
        else:
            words = f.read().splitlines()
    return words


def write_words_to_file(file_path, arr):
    """

    :param file_path:
    :param arr:
    """
    # Open and write to file path passed
    with open(file_path, 'w', encoding='utf-8-sig') as f:
        string = '\n'.join(arr)
        f.write(string)
    # Mark EOF
    pass


def load_w2v(fn='google_w2v_weights/GoogleNews-vectors-negative300.bin.gz'):
    """

    :param fn:
    :return:
    """
    print(f"Loading Word2Vec model...")
    rv = None
    if fn.__contains__('.bin.gz'):
        rv = KeyedVectors.load_word2vec_format(fn, binary=True)
    elif fn.__contains__('.model'):
        rv = Word2Vec.load(fn)
    print(f"Loaded Word2Vec model!\n")
    return rv


def expand_set(model_fp='google_w2v_weights/GoogleNews-'
                        'vectors-negative300.bin.gz',
               entity_set_fp='data_prep/entity_set.txt',
               entity_set=None,
               out=True,
               output_fn='expansion_set_2'):
    """
    This function loads a specified W2V model, reads and loads an entity set
    from a pickle file and convert it to a list.
    Then for each word in the entity set it appends the word and most similar
    word returned from the W2V model.
    :param entity_set: set - the set of words which to expand on.
    :param model_fp: str - file path pointing to weights to be loaded.
    :param entity_set_fp: (str||None) - file path pointing to set to be loaded.
    :param out: bool - if true then the function will print info otherwise nothing
    will be outted to the console.
    :param output_fn: str - file name of the output_set_expansion to be stored and written to
    :return: a list of pairs where each pair contains the original word and
    the most similar word generated by the W2V model.
    """
    # Load a pre-trained Word2Vec model
    model = load_w2v(fn=model_fp)
    # Set state representing model type
    pre_trained = False
    if model_fp.__contains__('.model'):
        pre_trained = True
    # Define the initial entity set
    if entity_set_fp is not None:
        entity_set = read_words_from_file(entity_set_fp)
    if out:
        list_info(entity_set)
    # Convert set to array
    entity_arr = list(entity_set)
    if out:
        list_info(entity_arr)
    # Expand the entity set
    expansion_arr = []
    for word in entity_set:
        try:
            if not pre_trained:
                similar_words_list = model.most_similar(word.lower())
            else:
                similar_words_list = [word for word in model.wv.most_similar(word.lower())]
        except KeyError:
            if out:
                print(f"'{word}' not present in W2V vocabulary.")
            continue
        # similar_words = [word[0] for word in model.most_similar(word, topn=num_similar_words)]
        # expansion_arr.append(f"{word}, {similar_words_list[0][0]}")
        similar_words_added = 0
        for i, v in enumerate(similar_words_list):
            if similar_words_added == 3:
                continue
            if word.lower() != v[0].lower():
                expansion_arr.append(f"{word}, {similar_words_list[i][0]}")
                similar_words_added += 1
    # The expanded entity set
    if out:
        list_info(expansion_arr)
    write_words_to_file(f"{output_fn}", expansion_arr)
    return expansion_arr


def w2v_transfer_learning(corpus_fp='data_prep/sentences_processed.pkl',
                          model_fn="google_trained_2.model"):
    """
    Note: this uses an experimental function from the gensim library.
    Although I got it to function it does not work or perform as intended.

    Loads the Google pre-trained model, trains the existing
    model on our corpus.
    :param corpus_fp: string - point to the filepath of the corpus
    :param model_fn: string - specify the save location and name of
        the saved weights for the transfer-learning model
    """
    # # Example corpus Todo: process my corpus to be like this
    # # corpus = [["dog", "cat", "fish"],\
    # #           ["car", "bus", "train"],\
    # #           ["apple", "banana", "cherry"]]
    #
    # # Load sentences from .pkl file
    # corpus = load_pickle_file(corpus_fp)
    # list_info(corpus)
    # # Create the Word2Vec model
    # model = Word2Vec(vector_size=300, min_count=1)
    # model.build_vocab(corpus)
    # # Prevent error # Todo: this might be wrong
    # model.wv.vectors_lockf = np.ones((100, 100), dtype=np.float32)
    # # Use experimental function to perform TL
    # model.wv.intersect_word2vec_format('google_w2v_weights/GoogleNews'
    #                                    '-vectors-negative300.bin.gz', binary=True)
    # model.train(corpus, total_examples=len(corpus), epochs=10)
    # # Save the model as pre-trained weights to load later
    # save_model(model, model_fn)
    # Mark EOF
    pass


def remove_punctuation(input_string):
    """

    :param input_string:
    :return:
    """
    # Create a string of all punctuation characters
    punctuation = string.punctuation
    # Replace all punctuation characters with an empty string
    no_punct = "".join([char for char in input_string if char not in punctuation])
    return no_punct


def store_pickle_file(obj, filename):
    """

    :param obj:
    :param filename:
    """
    with open(filename, 'wb') as f:
        pickle.dump(obj, f)


def load_pickle_file(filename):
    """
    Passed a filename or path to a pickle file the
    object is loaded and returned.
    """
    with open(filename, 'rb') as f:
        obj = pickle.load(f)
    return obj


def list_info(arr):
    """ Out information about the passed list. """
    if isinstance(arr, list):
        print(f"List contains {len(arr)} items.")
    elif isinstance(arr, set):
        print(f"Set contains {len(arr)} items.")
    print(f"First 5 items:[")
    for item in list(arr)[:5]:
        print(f"'{item}',")
    print(f"]\n")
    # Mark EOF
    pass


def extract_words(sentences_list):
    """
    Passed a list of sentences this function extracts
    a list of words and a set unique words, both of which
    are returned.
    """
    words_ = []
    for arr in sentences_list:
        for i, word in enumerate(arr.split()):
            words_.append(word.strip().lower())
    # list_info(words)
    # Extract unique words from sentences
    words_set_ = set(words_)
    list_info(words_set_)
    return words_, words_set_


def preprocess_sentences(sentences_list):
    """
    Remove sentences with less than 10 words.
    Remove punctuation.
    :return: cleaned list of sentences
    """
    # Remove headers, titles, etc.etc
    sentences_list = [element for element in sentences_list if len(element.split()) >= 10]
    # Remove punctuation
    for i, string in enumerate(sentences_list):
        sentences_list[i] = remove_punctuation(string.lower())
    # Return pre-processed
    return sentences_list


if __name__ == '__main__':

    # Mark end of if-name-main section
    pass
