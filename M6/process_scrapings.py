# Author: Lee Taylor
import pickle
import re
from w2v import read_words_from_file


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


def remove_punctuation(text):
    """
    Removes all punctuation from a string.

    :param text: A string to remove punctuation from.
    :return: A string with all punctuation removed.
    """
    # Use a regular expression to match all characters that are not letters or numbers
    return re.sub(r'[^\w\s]', '', text)


def smart_replace(big_string_):
    """

    :param big_string_:
    :return:
    """
    # Type check
    if not isinstance(big_string_, str):
        raise TypeError("Param: 'big_string' should be a string!")
    # Convert big_string to a list of chars
    chars = list(big_string_)
    # Remove fullstops not used to end sentences
    #   and remove newline chars
    new_chars = []
    for i, c in enumerate(chars):
        # Fullstop used to end sentence
        if c == '.' and chars[i+1] == ' ':
            new_chars.append(c)
        # Fullstop not used to end sentence
        elif chars[i-1] != ' ' and c == '.' and chars[i+1] != ' ':
            new_chars.append(',')
        elif c == '\n':
            new_chars.append(' ')
        else:
            new_chars.append(c)
    new_big_string_ = ''.join(new_chars)
    return new_big_string_


def extract_sentences(big_string_):
    """
    Removing casing and seperate into sentences on fullstop chars.
    :param big_string_:
    :return:
    """
    rv = []
    sentences_ = big_string_.split('.')
    for sentence in sentences_:
        sentence = sentence.lower()
        sentence = remove_punctuation(sentence)
        if len(sentence.split()) >= 10:
            rv.append(sentence.split())
    return rv


if __name__ == '__main__':
    # Read list of words to search
    entity_set = read_words_from_file('data_prep/entity_set.txt')
    # Parse webapage for text
    for word in entity_set:
        with open(f"scrapings_copy/wikipedia {word}.txt", "r",
                  encoding='utf-8-sig') as f:
            lines = f.readlines()

        # Remove fullstops
        big_string = smart_replace(''.join(lines))
        sentences = extract_sentences(big_string)
        # print(sentences)
        store_pickle_file(sentences,
                          f"scrapings_sentences/wikipedia {word}.pkl"
                          )

    # Mark end of if-name-main-section
    pass
