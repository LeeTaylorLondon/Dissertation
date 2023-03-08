# Author: Lee Taylor
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
import gensim
import gzip
import shutil


def read_words_from_file(file_path):
    with open(file_path, 'r') as f:
        words = set(f.read().splitlines())
    return words

def unzip_gz():
    with gzip.open('GoogleNews-vectors-negative300.bin.gz', 'rb') as f_in:
        with open('GoogleNews-vectors-negative300.bin', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

# Load a pre-trained Word2Vec model
# model = Word2Vec.load(
#     'GoogleNews-vectors-negative300.bin'
# )

# Load a pre-trained Word2Vec model
gensim.models.KeyedVectors.load_word2vec_format(
    'GoogleNews-vectors-negative300.bin', encoding='binary'
)

# Define the initial entity set
# entity_set = {"clothing", "fashion", "apparel", "garment", "outfit"}
entity_set = read_words_from_file("pt_entity_set")

# Define the number of similar words to add to the entity set
num_similar_words = 100

# Expand the entity set
for word in entity_set:
    similar_words = [word[0] for word in model.wv.most_similar(word, topn=num_similar_words)]
    entity_set.update(similar_words)

# The expanded entity set
print(entity_set)
