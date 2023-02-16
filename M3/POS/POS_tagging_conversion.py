import nltk

# First, you need to download the necessary resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def convert_to_readable_tags(tagged_sentence):
    readable_tags = {
        'CC': 'coordinating conjunction',
        'CD': 'cardinal digit',
        'DT': 'determiner',
        'EX': 'existential there',
        'FW': 'foreign word',
        'IN': 'preposition/subordinating conjunction',
        'JJ': 'adjective',
        'JJR': 'adjective, comparative',
        'JJS': 'adjective, superlative',
        'LS': 'list marker',
        'MD': 'modal',
        'NN': 'noun, singular or mass',
        'NNS': 'noun, plural',
        'NNP': 'proper noun, singular',
        'NNPS': 'proper noun, plural',
        'PDT': 'predeterminer',
        'POS': 'possessive ending',
        'PRP': 'personal pronoun',
        'PRP$': 'possessive pronoun',
        'RB': 'adverb',
        'RBR': 'adverb, comparative',
        'RBS': 'adverb, superlative',
        'RP': 'particle',
        'SYM': 'symbol',
        'TO': 'to',
        'UH': 'interjection',
        'VB': 'verb, base form',
        'VBD': 'verb, past tense',
        'VBG': 'verb, gerund/present participle',
        'VBN': 'verb, past participle',
        'VBP': 'verb, non-3rd person singular present',
        'VBZ': 'verb, 3rd person singular present',
        'WDT': 'wh-determiner',
        'WP': 'wh-pronoun',
        'WP$': 'possessive wh-pronoun',
        'WRB': 'wh-adverb'
    }

    readable_sentence = [(word, readable_tags.get(tag, tag)) for word, tag in tagged_sentence]

    return readable_sentence


sentence = "NLTK is a popular Python library for NLP."
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)

readable_tagged = convert_to_readable_tags(tagged)

print(readable_tagged)
