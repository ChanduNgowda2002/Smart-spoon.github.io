import os
import numpy as np
from tensorflow.keras.preprocessing import image
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf

def load_food101_images(data_dir):
    X = []
    y = []
    
    # Creating a label map from folder names (food categories)
    label_map = {label: idx for idx, label in enumerate(sorted(
        [d for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))]
    ))}
    
    print(f"Label map: {label_map}")

    # Looping through each food folder (category)
    for food in os.listdir(data_dir):
        food_folder = os.path.join(data_dir, food)
        
        if os.path.isdir(food_folder):  # Only process directories (food categories)
            for img_name in os.listdir(food_folder):
                img_path = os.path.join(food_folder, img_name)
                
                try:
                    # Load and resize the image
                    img = image.load_img(img_path, target_size=(64, 64))  # You can adjust the size
                    img_array = image.img_to_array(img)
                    
                    # Normalize and append to data list
                    X.append(img_array)
                    y.append(label_map[food])  # Label from the label_map
                    
                except Exception as e:
                    print(f"❌ Skipping corrupted image: {img_path} | Error: {e}")
    
    # Convert lists to numpy arrays for model input
    X = np.array(X, dtype='float32')
    X /= 255.0  # Normalize images to [0, 1]
    
    y = np.array(y, dtype='int')
    
    return X, y, label_map

# Example usage
data_dir = './food-101/images'  # Change to the correct directory path
X, y, label_map = load_food101_images(data_dir)

# Save the processed data as numpy arrays for later use
np.save('X.npy', X)
np.save('y.npy', y)
np.save('label_map.npy', label_map)

print(f"Processed {len(X)} images.")
