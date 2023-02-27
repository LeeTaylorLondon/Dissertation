import nltk

# Download the necessary resources
# tokenizer
nltk.download('punkt')
# labels words for corresponding grammatical category
nltk.download('averaged_perceptron_tagger')

# tokenize the sentence into words
sentence = "NLTK is a popular Python library for NLP."
tokens = nltk.word_tokenize(sentence)

# Then, you can perform POS tagging
tagged = nltk.pos_tag(tokens)

# Finally, you can extract all of the nouns using a conditional statement
nouns = [word for word, pos in tagged if pos in ['NN', 'NNS', 'NNP', 'NNPS']]

# The result is a list of all of the nouns in the sentence
print(nouns)

# Prints
# >>> ['NLTK', 'Python', 'library', 'NLP']
