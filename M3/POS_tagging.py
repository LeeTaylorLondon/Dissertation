import nltk

# Download the necessary resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Tokenize the sentence into words
sentence = "NLTK is a popular Python library for NLP."
tokens = nltk.word_tokenize(sentence)

# Perform POS tagging
tagged = nltk.pos_tag(tokens)

# Result is a list of tuples, where each tuple contains a word and its corresponding tag
print(tagged)
