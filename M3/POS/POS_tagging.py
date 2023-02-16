import nltk

# First, you need to download the necessary resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Next, you need to tokenize the sentence into words
sentence = "NLTK is a popular Python library for NLP."
tokens = nltk.word_tokenize(sentence)

# Then, you can perform POS tagging
tagged = nltk.pos_tag(tokens)

# The result is a list of tuples, where each tuple contains a word and its corresponding tag
print(tagged)
