from tensorflow.keras.models import load_model
import pickle
import numpy as np

model = load_model('html_model.h5')
tokenizer = pickle.load(open('html_tokens.pl', 'rb'))

def predict(text):
    sequence = tokenizer.texts_to_sequences([text])
    sequence = np.array(sequence)
    preds = np.argmax(model.predict(sequence))
    predicted_word = ''
    
    for key, val in tokenizer.word_index.items():
        if val == preds:
            predicted_word = key
            break
    
    return predicted_word
