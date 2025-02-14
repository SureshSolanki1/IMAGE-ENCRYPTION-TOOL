from PIL import Image
import numpy as np
import os

def encrypt_image(input_path, output_path, key):
    print(f"Encrypting {input_path} with key {key}")
    image = Image.open(input_path)
    image_array = np.array(image)
    print("Image array shape:", image_array.shape)

    np.random.seed(key)
    key_matrix = np.random.randint(0, 256, image_array.shape, dtype=np.uint8)
  
    encrypted_array = np.bitwise_xor(image_array, key_matrix)
    encrypted_image = Image.fromarray(encrypted_array)
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    print(f"Decrypting {input_path} with key {key}")
    image = Image.open(input_path)
    encrypted_array = np.array(image)

    np.random.seed(key)
    key_matrix = np.random.randint(0, 256, encrypted_array.shape, dtype=np.uint8)

    decrypted_array = np.bitwise_xor(encrypted_array, key_matrix)
    decrypted_image = Image.fromarray(decrypted_array)
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

if __name__ == "__main__":
    input_path = "D:\\Projects\\velvet_Shimmer.jpg"   # Change this to your actual image path
    encrypted_path = "D:\\Projects\\encrypted.png"
    decrypted_path = "D:\\Projects\\decrypted.png"
    key = 1234  # Change the key to any integer

    print("Starting Encryption...")
    encrypt_image(input_path, encrypted_path, key)

    print("Starting Decryption...") 
    decrypt_image(encrypted_path, decrypted_path, key)

