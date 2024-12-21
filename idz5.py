from PIL import Image

# Path to the latest uploaded file
image_path = "/mnt/data/image.png"

# Open the image to verify its content before proceeding to any edits or notes
img = Image.open(image_path)
img.show()


