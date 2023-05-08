from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint
import pickle
import numpy as np

from config import *

# Read Data
data = open(text_file, 'r', encoding='utf-8').read()
data = data.lower().replace('\n', ' ')
data = data.split()
data = ' '.join(data)

# Tokenize
tokenizer = Tokenizer(oov_token='OOV')
tokenizer.fit_on_texts([data])
pickle.dump(tokenizer, open(token_filename, 'wb'))
sequence_data = tokenizer.texts_to_sequences([data])[0]

# Get the Size of the Vocabulary
vocab_size = len(tokenizer.word_index) + 1

# Generate the sequences of words
sequences = []
for i in range(window, len(sequence_data)):
    words = sequence_data[i-window:i+1]
    sequences.append(words)
sequences = np.array(sequences)
sequences[:10]

# Split in training data
X = []
y = []
for i in sequences:
    X.append(i[0:window])
    y.append(i[window])
X = np.array(X)
y = np.array(y)
y = to_categorical(y, num_classes=vocab_size)

# Create Model
model = Sequential()
model.add(Embedding(vocab_size, 10, input_length=window))
model.add(LSTM(1000, return_sequences=True))
model.add(LSTM(1000))
model.add(Dense(1000, activation=activation))
model.add(Dense(vocab_size, activation=output_activation))

# Train
checkpoint = ModelCheckpoint(model_name, monitor='loss', verbose=1, save_best_only=True)
model.compile(loss=loss, optimizer=Adam(learning_rate=learning_rate))
model.fit(X, y, epochs=epochs, batch_size=batch_size, callbacks=[checkpoint])
