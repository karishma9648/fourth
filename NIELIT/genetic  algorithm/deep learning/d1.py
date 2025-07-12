import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

np.random.seed(42)
X_train = np.random.rand(1000, 10)
Y_train = np.random.randint(2, size=(1000, 1))

model = Sequential([
    Dense(10, activation='relu', input_shape=(10,)),
    Dense(10, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X_train, Y_train, epochs=10, batch_size=32)

test_data = np.random.rand(10, 10)
predictions = model.predict(test_data)
print(predictions)