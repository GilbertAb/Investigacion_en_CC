import data_extract

corpus = []
def main():
    corpus.append(getSentences(filename='test/test.html'))
    corpus.append(getSentences(filename='test/test2.html'))
    print(corpus)
    '''filename = 'test/test.html'
    # Read html file
    html = data_extract.read_html_file(filename)
    #  Parsed Tags
    parsed_tags = data_extract.generate_parsed_tags(html)
    # Generated corpus
    corpus = data_extract.generate_corpus(parsed_tags)
    for i in range(1,10):
        sentences.append(corpus.split(" "))
    print(sentences)'''

def getSentences(filename):
    # Read html file
    html = data_extract.read_html_file(filename)
    #  Parsed Tags
    parsed_tags = data_extract.generate_parsed_tags(html)
    # Generated corpus
    corpus = data_extract.generate_corpus(parsed_tags)
    sentences = corpus.split(" ")
    print(sentences)
    return sentences
if __name__ == '__main__':
    main()


#######################################################################
import re  # For preprocessing
import pandas as pd  # For data handling
from time import time  # To time our operations
from collections import defaultdict  # For word frequency

import spacy  # For preprocessing

import logging  # Setting up the loggings to monitor gensim
logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M:%S', level=logging.INFO)

import multiprocessing

from gensim.models import Word2Vec

''' 
Step 1: Word2Vec()
    Set up the parameters of the model one-by-one
    Don't supply the parameter sentences, to leave the model uninitialized
'''
'''
Step 2: .build_vocab()
    Build the voacabulary from a sequence of sentences and thus 
    initialized the model
    With the loggings, can follow the progress and the effect of
    "min_count" and "sample" on the word corpus
'''
'''
Step 3: .train()
    Train the model.
    The loggings here are useful for monitoring.
'''

cores = multiprocessing.cpu_count() # Count the number of cores in a computer

''' 
Step 1: Word2Vec()
    Set up the parameters of the model one-by-one
    Don't supply the parameter sentences, to leave the model uninitialized
'''
'''
    min_count (int) = ignores all words with total absolute frequence lower than this 
    window (int) = maximum distance between current and predicted word within a sentence
    size (int) = dimensionality of the feature vectors
    sample (float) = Threshold for configuring which higuer frequency words are randomly downsampled. Highly influencial
    alpha (float) = Initial learning rate
    min_alpha (float) = Learning rate will linearly drop to min_alpha as training progresses.
    negative (int) = if > 0, negative sampling will be used. Specifies how many "noise words" should be drown.
    workers (int) = Use these many worker threads to train the model.
'''
min_count = 2
window = 2
size = 3
sample = 6e-5
alpha = 0.03
min_alpha = 0.0007
negative = 20
workers = cores -1 

w2v_model = Word2Vec(min_count=min_count, window=window, vector_size=size,
                     sample=size, alpha=alpha, min_alpha=min_alpha, negative=negative,
                     workers=workers)

'''
Step 2: .build_vocab()
    Build the voacabulary from a sequence of sentences and thus 
    initialized the model
    Build the table digesting all the words and filtering out the
    unique words and doing some basic count on them.
'''
t = time()

w2v_model.build_vocab(corpus, progress_per=1)

print('Time to build vocab: {} mins'.format(round((time() - t) / 60, 2)))

'''
Step 3: .train()
    Train the model.
'''
'''
    total_examples (int) = Count of sentences.
    epochs (int) = Number of iterations over the corpus.
'''
t = time()

w2v_model.train(corpus, total_examples=w2v_model.corpus_count, epochs=30, report_delay=1)

print('Time to train the model: {} mins'.format(round((time() - t) / 60, 2)))

'''
    As we do not plan to train the model any further, we are
    calling init_sims(), which will make the model much more
    memory-efficient:
'''
#w2v_model.init_sims(replace=True)

print("Most Similar to story: ")
print(w2v_model.wv.most_similar(positive=["story"]))


