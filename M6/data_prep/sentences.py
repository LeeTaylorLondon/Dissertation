"""
Author: Lee Taylor

"""
from ..functions_ import *


if __name__ == '__main__':
    # Extract and stored sentences as a loadable file
    # sentences = extract_sentences("books_xml")
    # store_pickle_file(sentences, 'sentences.pkl')
    # print("Stored object 'sentences' as 'sentences.pkl'.")

    # # Load sentences from .pkl file and reduce sentences
    # sentences = load_pickle_file('sentences.pkl')
    # list_info(sentences) # 239.5K Sentences

    # # Preprocess sentences
    # sentences_p = preprocess_sentences(sentences)
    # print("Pre-processed sentences.")
    # list_info(sentences_p) # 167.5K Sentences

    # # Store pre-processed sentences
    # store_pickle_file(sentences_p, 'sentences_processed.pkl')

    # Load sentences from .pkl file and reduce sentences
    sentences_p = load_pickle_file('sentences_processed.pkl')
    list_info(sentences_p)  # 167.5K Sentences

    # Extract all words and unique words
    print("Unique words.")
    words, words_set = extract_words(sentences_p)

    # Store unique words
    store_pickle_file(words_set, 'unique_words.pkl')

    # Mark end of 'main' section
    pass
