from PIL import Image
import os

def resize_image(input_path, output_path, size):
    img = Image.open(input_path)
    img_resized = img.resize(size)
    img_resized.save(output_path)

input_path = input("Enter the path to the image file: ")
output_path = input("Enter the path where the resized image file will be saved: ")
width = int(input("Enter the width of the resized image: "))
height = int(input("Enter the height of the resized image: "))

resize_image(input_path, output_path, (width, height))

print("Image resized successfully!")
