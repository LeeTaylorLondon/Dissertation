# Author: Lee Taylor
from functions_ import *


if __name__ == '__main__':
    # # Load sentences from .pkl file and reduce sentences
    # sentences_p = load_pickle_file('data_prep/sentences_processed.pkl')
    # list_info(sentences_p)  # 167.5K Sentences

    # # Train W2V and save model
    # corpus = sentences_p
    # model = train_model(corpus)
    # save_model(model, "word2vec_2.model")

    # Load google model and train it on our corpus
    # w2v_transfer_learning()

    # # Expand an entity set
    # expand_set()

    """
    def expand_set(
            model_fp='word2vec.model', 
            entity_set_fp='data_prep/entity_set.txt',
            out=True, 
            output_fn='expansion_set_2'
        ):
    """
    expand_set(
        model_fp='model_weights/mit_wiki_model.model',
        output_fn='expansion_set_mit_wiki.txt'
    )

    # expand_set(output_fn='expansion_set_google')

    """ Load sentences then train and save a model """
    # sentences = load_pickle_file("scrapings_sentences/all sentences.pkl")
    # model = train_model(sentences)
    # save_model(model, "mit_wiki_model.model")

    # Mark end of if-name-main-section
    pass


