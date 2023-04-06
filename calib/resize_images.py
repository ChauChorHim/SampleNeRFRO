import os
from PIL import Image

# Set the input and output directories
input_dir = "D:/dev/thesis/data/real/Beetles/raw/"
output_dir = "D:/dev/thesis/data/real/Beetles/images/"

# Set the scaling factor
scaling_factor = 0.15 # resize the image to 50% of its original size

# Loop through each file in the input directory
for filename in os.listdir(input_dir):
    # Check if the file is a CR2 image
    if filename.endswith(".CR2"):
        # Open the CR2 image file
        with Image.open(os.path.join(input_dir, filename)) as im:
            # Calculate the new dimensions based on the scaling factor
            width, height = im.size
            new_width = int(width * scaling_factor)
            new_height = int(height * scaling_factor)
            # Resize the image to the new dimensions
            im_resized = im.resize((new_width, new_height))
            # Set the output filename with the PNG file extension
            output_filename = os.path.splitext(filename)[0] + ".png"
            # Save the resized image as a PNG file in the output directory
            im_resized.save(os.path.join(output_dir, output_filename), "PNG")