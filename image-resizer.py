from PIL import Image

def resize_image(input_path, output_path, new_width, new_height):
    # Open the image
    image = Image.open(input_path)

    # Resize the image
    resized_image = image.resize((new_width, new_height))

    # Save the resized image
    resized_image.save(output_path)

    print("Image resized successfully.")

# Usage
input_path = "picture.png"  # Path to the input image file
output_path = "output.png"  # Path to save the resized image
new_width = 800  # Desired width for the resized image
new_height = 1200  # Desired height for the resized image

resize_image(input_path, output_path, new_width, new_height)

