#Importing necessary libraries

import numpy as np
import tensorflow as tf 
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

#Load the MNIST dataset
(train_images,trainlables), (test_images,test_lables)=datasets.mnist.load_data()

#normalizing the images to a range of 0 to 1
train_images=train_images/255.0
test_images=test_images/255.0

#Reshape the images to 28x28x1
train_images=train_images.reshape((train_images.shape[0],28,28,1))
test_images=test_images.reshape((test_images.shape[0],28,28,1))

#convert the labels to one-hot encoded format
trainlables = to_categorical(trainlables)
test_lables = to_categorical(test_lables)

# building the CNN model
model = models.Sequential()

#first convolutional layer
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2,2)))

#second convolutional layer
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2,2)))

#third convolutional layer
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2,2)))

#Flatten the 3D oytput to 1D and add a Dense layer
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))

#output layer with 10 neurons for 10 digit classes
model.add(layers.Dense(10, activation='softmax'))

#compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

#train the model
model.fit(train_images, trainlables, epochs=5, batch_size=64, validation_data=(test_images, test_lables))

#evaluate the model on the test data
test_loss, test_acc = model.evaluate(test_images, test_lables)
print(f"Test accuracy:{test_acc*100:.2f}%")

#make predictions on the test images
predictions = model.predict(test_images)
print(f"prediction for first test image: {np.argmax(predictions[4])}")

plt.imshow(test_images[4].reshape(28,28), cmap='gray')
plt.title(f"Predicted label: {predictions[4].argmax()}")

plt.show()