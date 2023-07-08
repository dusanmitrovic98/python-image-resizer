from PIL import Image

def resize_image(input_path, output_path, new_width, new_height):
    # Open the image
    image = Image.open(input_path)

