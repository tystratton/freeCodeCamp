import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from keras import datasets, layers, models #image and imagedatagenerator are for data augmentation



# Load and split dataset
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

# Let's look at a one image
# IMG_INDEX = 7  # change this to look at other images

# plt.imshow(train_images[IMG_INDEX] ,cmap=plt.cm.binary)
# plt.xlabel(class_names[train_labels[IMG_INDEX][0]])
# plt.show()

# # Let's look at a one image
# IMG_INDEX = 7  # change this to look at other images

# plt.imshow(train_images[IMG_INDEX] ,cmap=plt.cm.binary)
# plt.xlabel(class_names[train_labels[IMG_INDEX][0]])
# plt.show()

# Convolutional base
# Extracts features
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2))) # 2 by 2, with a stride of 2
model.add(layers.Conv2D(64, (3, 3), activation='relu')) # Figures out size from previous layer, activation function squishes values to 0 to infinity
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

# model.summary()  # let's have a look at our model so far

#Classifier
# Adding dense layers to classify features from convolutional base

model.add(layers.Flatten()) # Take 4,4,64, put them in a straight line
model.add(layers.Dense(64, activation='relu')) # 64 node layer that connects to input
model.add(layers.Dense(10)) #amount of classs in the problem

model.summary()
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

history = model.fit(train_images, train_labels, epochs=4, 
                    validation_data=(test_images, test_labels))

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print(test_acc)
model.save('C://Users/tystratt/Desktop/freeCodeCamp/Machine Learning with Python/covnet_model.keras')

# Data Augmentation 
# To avoid overfitting and create a larger dataset fro you perform random transformations
# on images so that the model generalizes better. Changes can be compressions, rotations,
# stretches, and color changes.