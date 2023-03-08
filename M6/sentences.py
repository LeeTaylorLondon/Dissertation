import os
import xml.etree.ElementTree as ET
import pickle
import string


def remove_punctuation(input_string):
    # Create a string of all punctuation characters
    punctuation = string.punctuation
    # Replace all punctuation characters with an empty string
    no_punct = "".join([char for char in input_string if char not in punctuation])
    return no_punct


def store_pickle_file(obj, filename):
    with open(filename, 'wb') as f:
        pickle.dump(obj, f)


def load_pickle_file(filename):
    with open(filename, 'rb') as f:
        obj = pickle.load(f)
    return obj


def list_info(arr):
    """ Out information about the passed list. """
    if isinstance(arr, list):
        print(f"List contains {len(arr)} items.")
    elif isinstance(arr, set):
        print(f"Set contains {len(arr)} items.")
    print(f"First 5 items: {list(arr)[:5]}.\n")
    # Mark EOF
    pass


def extract_sentences(directory: str):
    """ Read .xml file for sentences marked with <s></s>.
    Returns a list of sentences as stirngs.
    """
    sentences = []
    for file in os.listdir(directory):
        # Parse XML file
        tree = ET.parse(os.path.join(directory, file))
        root = tree.getroot()
        # Find all elements with tag 's'
        for s in root.findall(".//s"):
            sentences.append(s.text)
    list_info(sentences)
    return sentences


def extract_words(sentences_list):
    """ Passed a list of sentences this function extracts
    a list of words and a set unique words, both of which
    are returned.
    """
    words = []
    for arr in sentences_list:
        for i, word in enumerate(arr.split()):
            words.append(word.strip().lower())
    # list_info(words)
    # Extract unique words from sentences
    words_set = set(words)
    list_info(words_set)
    return words, words_set


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
    # Extract and stored sentences as a loadable file
    # sentences = extract_sentences("en")
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
    list_info(sentences_p) # 167.5K Sentences

    # Extract all words and unique words
    print("Unique words.")
    words, words_set = extract_words(sentences_p)

    # Store unique words
    store_pickle_file(words_set, 'unique_words.pkl')

    # Mark end of 'main' section
    pass
