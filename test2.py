import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow import keras


fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
# print(train_images.shape)
# type(train_images) #find type of images

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

#creates figure of iamge
# plt.figure()
# plt.imshow(train_images[1])
# plt.colorbar()
# plt.grid(False)
# plt.show()

#data preprocessing, puts values between 0 and 1
train_images = train_images / 255.0
test_images = test_images / 255.0

loaded_model = tf.keras.models.load_model('clothes model.h5')

tf.keras.Model.save('C:/Users/tystratt/Desktop/freeCodeCamp/Machine Learning with Python/clothes model.keras')
# model.fit(train_images, train_labels, epochs=10)

test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=1)
print('Test accuracy:', test_acc)