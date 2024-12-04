import tensorflow as tf
from tensorflow import keras
from keras.preprocessing import sequence
from keras.datasets import imdb
import numpy as np

VOCAB_SIZE = 88584

MAXLEN = 250
BATCH_SIZE = 64

# Dataset 1 is most common word, 88584 is least common word
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words = VOCAB_SIZE)

# Padding data to 250, or trimming it to 250
train_data = sequence.pad_sequences(train_data, MAXLEN)
test_data = sequence.pad_sequences(test_data, MAXLEN)

model = tf.keras.Sequential({
    tf.keras.layers.Embedding(VOCAB_SIZE, 32), # creates vectors
    tf.keras.layers.LSTM(32), # 32 dimensions for every word
    tf.keras.layers.Dense(1, activation="sigmoid")
})

#TRAINING
model.compile(loss="binary_crossentropy", optimizer="rmsprop", metrics=['acc'])

history = model.fit(train_data, train_labels, epochs = 10, validation_split = 0.2)

word_index = imdb.get_word_index()

def encode_text(text):
    tokens = keras.preprocessing.text.text_to_word_sequence(text)
    tokens = [word_index[word] if word in word_index else 0 for word in tokens]
    return sequence.pad_sequences([tokens], MAXLEN)[0]

text = "that move was just amazing, so amazing"
encoded = encode_text(text)
print(encoded)