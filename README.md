# IMAGE-ENCRYPTION-TOOL
Pixel Manipulation for Image Encryption

### Overview

This code provides functionality to encrypt and decrypt images using a simple method based on the XOR (exclusive or) operation. It uses Python Imaging Library (PIL) to handle image files and NumPy to work with image data in array form. The encryption and decryption processes use the same key, demonstrating a symmetric encryption method.

### Key Components

#### 1\. Import Statements

```python
from PIL import Image
import numpy as np
import os
```

* **PIL (Pillow)**: A library used for opening, manipulating, and saving many different image file formats.
* **NumPy**: A library for numerical computing. In this code, it is used to create array representations of images and perform operations on those arrays.
* **os**: Although imported, the `os` module is not specifically used in this code snippet but is commonly used for file operations.

#### 2. `encrypt_image` Function

```python
def encrypt_image(input_path, output_path, key):
```

* **Parameters**:
    * `input_path`: Path to the image to be encrypted.
    * `output_path`: Path where the encrypted image will be saved.
    * `key`: An integer that initializes the random number generator to ensure reproducibility.

##### Inside the Function:

1. **Open and Convert Image**:

    ```python
    image = Image.open(input_path)
    image_array = np.array(image)
    ```
    * Opens the image specified by `input_path` and converts it into a NumPy array for processing.
2. **Generate Key Matrix**:

    ```python
    np.random.seed(key)
    key_matrix = np.random.randint(0, 256, image_array.shape, dtype=np.uint8)
    ```
    * Sets the seed for random number generation based on the provided `key`. This ensures that the same key will produce the same random numbers each time.
    * Creates a matrix (`key_matrix`) of the same shape as the image, filled with random integers between 0 and 255 (inclusive), which represents possible pixel values.
3. **Encrypt Image**:

    ```python
    encrypted_array = np.bitwise_xor(image_array, key_matrix)
    ```
    * Applies the XOR operation between the original image array and the `key_matrix`. This transforms each pixel value by flipping bits based on the corresponding pixel value in the `key_matrix`, effectively encrypting the image.
4. **Save Encrypted Image**:

    ```python
    encrypted_image = Image.fromarray(encrypted_array)
    encrypted_image.save(output_path)
    ```
    * Converts the encrypted array back into an image and saves it to the `output_path`.

#### 3. `decrypt_image` Function

```python
def decrypt_image(input_path, output_path, key):
```

* **Parameters**:
    Similar to `encrypt_image`, it takes `input_path`, `output_path`, and `key`.

##### Inside the Function:

1. **Open Encrypted Image**:

    ```python
    image = Image.open(input_path)
    encrypted_array = np.array(image)
    ```
    * Opens the previously encrypted image and converts it to a NumPy array.
2. **Generate Key Matrix**:

    ```python
    np.random.seed(key)
    key_matrix = np.random.randint(0, 256, encrypted_array.shape, dtype=np.uint8)
    ```
    * Uses the same seed as in the encryption, generating the same random values so that we can properly decrypt the image.
3. **Decrypt Image**:

    ```python
    decrypted_array = np.bitwise_xor(encrypted_array, key_matrix)
    ```
    * Again applies the XOR operation; since XORing the same values results in the original value, this successfully decrypts the image.
4. **Save Decrypted Image**:

    ```python
    decrypted_image = Image.fromarray(decrypted_array)
    decrypted_image.save(output_path)
    ```
    * Converts the decrypted array back to an image and saves it.

### Main Block

```python
if __name__ == "__main__":
```

* Ensures that the following code block runs only if the script is executed directly (not imported as a module).

#### Input Path Configuration

```python
input_path = "D:\\Projects\\velvet_Shimmer.jpg"
encrypted_path = "D:\\Projects\\encrypted.png"
decrypted_path = "D:\\Projects\\decrypted.png"
key = 1234  # Change the key to any integer
```

* Defines the paths for input, encrypted output, and decrypted output images, as well as a key for the process.

#### Function Calls

```python
print("Starting Encryption...")
encrypt_image(input_path, encrypted_path, key)

print("Starting Decryption...") 
decrypt_image(encrypted_path, decrypted_path, key)

- Calls `encrypt_image` followed by `decrypt_image`, demonstrating the full cycle of the encryption/decryption process while printing the status at each step.

### Summary
This code provides a basic form of image encryption using a symmetric key and random key matrix. It uses well-established libraries to handle images and random number generation, showcasing how image data can be manipulated at the pixel level. The XOR operation ensures that each pixel value is transformed uniquely based on the key, making it a straightforward yet effective encryption method.
```
If you find any problems, you can reach out to me - sureshsolanki9808@gmail.com
