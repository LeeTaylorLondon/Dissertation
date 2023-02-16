# Author: Lee Taylor, ST #: 190211479
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings
import gensim
from gensim.models import Word2Vec


# [1] Load english literature lines
words, lines, sens = [], [], []
function_words = ['a', 'an', 'and', 'are', 'as', 'at', 'be',
                  'by', 'for', 'from', 'has',
                  'he', 'in', 'is', 'it', 'its',
                  'of', 'on', 'that', 'the', 'to',
                  'was', 'were', 'will', 'with', 'my',
                  'your', 'this', 'can']
with open("Data/The Great Gatsby.txt") as f:
    lines = f.readlines()
    for i, v in enumerate(lines):
        lines[i] = v.strip()
        sens.append([v.strip()])
        sens[i] = sens[i][0].split()
        words_ = lines[i].split()
        for w in words_:
            w = w.replace("â", "")
            w = w.replace("€", "")
            w = w.replace("˜", "")
            w = w.strip()
            w = w.lower()
            if w in function_words:
                continue
            words.append(w)

# [1.1] Create a set of words (use set as no words are repeated)
word_set = set(words)

# [2] Define the set `HPT` to contain words describing Human/Personality Traits
# hpt = ("openness", "conscientiousness", "extraversion", "agreeableness", "neuroticism")
hpt = ("happy", "sad")

# Create CBOW model
min_count   = 3
vector_size = 10
window      = 8
model1 = gensim.models.Word2Vec(sens, min_count=min_count,
                                vector_size=vector_size, window=window)
model1.train(sens, total_words=len(word_set), epochs=model1.epochs)
def calc_sim(w1, w2):
    return model1.wv.similarity(w1, w2)

# Similarity for each word
similarity_threshold = 0.989
lexicon = []
for bfw in hpt:
    for word in word_set:
        try:
            simi_ = calc_sim(word, bfw)
            # print(f"{word} {bfw} {calc_sim(word, bfw)}")
            if simi_ > similarity_threshold:
                lexicon.append(word)
        except:
            # print(f"Not found {bfw}")
            pass

print(f"\nWord Seed Set: {hpt}\n"
      f"\nWord2Vec HYPER-PARAMETERS: Min_count: {min_count}, "
      f"Vec_size: {vector_size}, Win_size: {window}\n"
      f"\n% Similarity Threshold: {similarity_threshold}\n"
      f"\nLexicon:")

offset = 20
for i in range(0, len(lexicon), offset):
    print(lexicon[i: i+offset])

"""
EXAMPLE OUTPUT: 

>>> Word Seed Set: ('happy', 'sad')
>>> 
>>> Word2Vec HYPER-PARAMETERS: Min_count: 3, Vec_size: 10, Win_size: 8
>>> 
>>> % Similarity Threshold: 0.989
>>> 
>>> Lexicon:
>>> ['hall', 'myself', 'met', 'together', 'them.', 
>>> 'dim', 'sad', 'taking', 'trembling', 'darkness.', 
>>> 'emerged', 'grotesque']
>>> 
>>> Process finished with exit code 0
"""

