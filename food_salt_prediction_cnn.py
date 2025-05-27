import os
import numpy as np
from tensorflow.keras.preprocessing import image
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from food101_loader import load_food101_images

# Define the path to your food-101 images directory
data_dir = '/home/chandu/Desktop/intern_app/food-101/images'  # Set the correct path

# Load the data
X, y, label_map = load_food101_images(data_dir)

# Ensure data is in the correct format
X = X.astype('float32')  # Ensure X is float32
X /= 255.0  # Normalize the images to [0, 1]
y = to_categorical(y, num_classes=len(label_map))  # One-hot encode the labels

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(len(label_map), activation='softmax')  # Output layer with the number of classes
])

# Compile the model
model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10, batch_size=32)

# Save the model
model.save('food_model.h5')

print("Model trained and saved successfully.")
