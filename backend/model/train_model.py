import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
import numpy as np

# Create model
def create_model():
    model = Sequential([
        Dense(512, activation='relu', input_shape=(1000,)),
        Dropout(0.3),
        Dense(256, activation='relu'),
        Dropout(0.3),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Generate dummy training data
X_train = np.random.rand(1000, 1000)
y_train = np.random.randint(0, 2, 1000)

model = create_model()
model.fit(X_train, y_train, epochs=5, batch_size=32)
model.save("resume_analyzer_model.h5")
