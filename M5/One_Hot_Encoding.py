# Author: Lee Taylor
# Source: https://www.educative.io/answers/one-hot-encoding-in-python
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder


def encode(text):
    # Split words
    if isinstance(text, str):
        text = text.split()
    # Encode words
    unique_words = set(text)
    encoder_dict = {}
    for i, word in enumerate(unique_words):
        encoder_dict.update({word: i})
    # Create one hot
    return_value = {}
    for word in unique_words:
        encoding = [0 for _ in range(len(unique_words))]
        encoding[encoder_dict.get(word)] = 1
        return_value.update({word: encoding})
    return return_value


def print_ohc(one_hot_encoding):
    for k, v in one_hot_encoding.items():
        print(f"{k}".ljust(15) + f"{v}")


if __name__ == '__main__':
    """ This code demonstrates how to 'one-hot encode (OHC)' as an NLP technique.
    OHC is the process of converting words into numerical vector representations. 
    Where the length of the vector is equal to the number of unique words in the phrase
    and the word encoded is represented with a 1 whilst the rest of the vector contains
    zeros. 
    Each dimension of the vector represents a unique word which can be passed to a 
    machine learning model. This techniques allows us to represent words in a numerical 
    form. """

    # Manual process made by Lee Taylor
    # Define text to 'one hot encode'
    text1 = 'I love researching Natural Language Processing!'
    ohc1 = encode(text1)
    print_ohc(ohc1)

    # Scikit-Learn example
    # Categorical data to be converted to numeric data
    colors = (["red", "green", "yellow", "red", "blue"])

    # integer mapping using LabelEncoder
    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(colors)
    print(integer_encoded)
    integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)

    # One hot encoding
    onehot_encoder = OneHotEncoder(sparse=False)
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded)

    print(onehot_encoded)
