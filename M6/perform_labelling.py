"""
Author: Lee Taylor

The purpose of this is to speed up labelling data.
"""
from sklearn.metrics import precision_score, recall_score, f1_score
from functions_ import *


def process_error():
    """
    Sample text.
    """
    # Load output
    words = read_words_from_file("output_set_expansion/labelled/eset_mit_wiki_.txt",
                                 rtype='list')
    corrected_words = []
    for word in words:
        print(word)
        word_ = word.replace(':', ',')
        corrected_words.append(word_)
    # Save labelling
    write_words_to_file("output_set_expansion/labelled/eset_mit_wiki_.txt",
                        corrected_words)
    # Mark EOF
    pass


def load_y():
    """
    Sample text.
    """
    # Read lines from file
    words = read_words_from_file("output_set_expansion/labelled/eset_mit_wiki_.txt",
                                 rtype='list')
    y_pred_ = []
    # Extract y prediction value from each line
    for word in words:
        y = word.split()[-1]
        y_pred_.append(int(y))
    # Return y predictions read from file
    return y_pred_


def main():
    """
    Sample text.
    """
    # Iterate over each file in the 'model_weights' directory
    for model_file in os.listdir("output_set_expansion/"
                                 "unlabelled_2"):
        # Create filepath string to model
        model_fp = os.path.join(
            "output_set_expansion/unlabelled_2/",
            model_file
        )
        print(model_fp)

        # Load output
        words = read_words_from_file(model_fp,
                                     rtype='list')

        # Label outputs
        words_labelled = []
        for word in words[:120]:
            try:
                label = int(input(f"{word}: "))
            except TypeError as e:
                print(e)
                label = -1
                pass
            words_labelled.append(f"{word}, {label}")

        # Save labelling
        write_words_to_file(f"output_set_expansion/"
                            f"labelled/"
                            f"{model_fp.split('/')[-1]}",
                            words_labelled)

    # Mark EOF
    pass


if __name__ == '__main__':
    main()
    # process_error()

    # y_pred = load_y()
    # y_true = [1 for _ in range(len(y_pred))]
    # # # Check if lengths are the same
    # # print(len(y_pred) == len(y_true))
    # # # >>> True
    #
    # # Calculate precision
    # precision = precision_score(y_true, y_pred)
    #
    # # Calculate recall
    # recall = recall_score(y_true, y_pred)
    #
    # # Calculate F1 score
    # f1 = f1_score(y_true, y_pred)
    #
    # print("K@3")
    # print("Recall: ", recall)
    # print("Precision: ", precision)
    # print("F1 Score: ", f1)

    # Mark EOF
    pass
