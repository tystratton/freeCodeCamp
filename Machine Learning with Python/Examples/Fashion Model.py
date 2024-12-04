import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras


fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
# print(train_images.shape)
# type(train_images) #find type of images

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', ' Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# creates figure of iamge
plt.figure()
plt.imshow(test_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

#data preprocessing, puts values between 0 and 1
train_images = train_images / 255.0
test_images = test_images / 255.0

# ------------------- CREATING MODEL
# model = keras.Sequential([
#     keras.layers.Flatten(input_shape=(28,28)), # input layer (1), flattens it into 784 pixels instead of a 28x28
#     keras.layers.Dense(128, activation='relu'), # hidden layer (2), 128 neurons, should be a little smaller than input layer
#     keras.layers.Dense(10, activation="softmax") # output layer (3), 10 output neurons, this matches how many class names there are, softmax makes values between 0 and 1
#     ])

# ------------------- COMPILING MODEL
# model.compile(optimizer='adam', # gradient descent
#               loss = 'sparse_categorical_crossentropy', # loss function
#               metrics = ['accuracy']) # what we want to see from network

# ------------------- LOADING MODEL
model = tf.keras.models.load_model('C://Users/tystratt/Desktop/freeCodeCamp/Machine Learning with Python/clothes_model.keras')

# ------------------- EVALUATING MODEL
# test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=1)

# -------------------- TRAINING
# model.fit(train_images, train_labels, epochs=8)

predictions = model.predict(test_images)
print(class_names[np.argmax(predictions[0])]) #finds max prediction probability from list, finds it in class

# -------------------- SAVING MODEL
model.save('C://Users/tystratt/Desktop/freeCodeCamp/Machine Learning with Python/clothes_model.keras') # used to save my model

# print('Test accuracy:', test_acc)