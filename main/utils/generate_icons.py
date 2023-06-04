import os
import json
from PIL import Image, ImageOps

# Intensity of the pastel effect (0.0 - 1.0)
pastel_intensity = 0.85

# Scale factor for the pictogram (0.0 - 1.0)
pictogram_scale = 0.6

# Read the colors from the JSON file
with open('colors.json', 'r') as file:
    colors = json.load(file)

# Create the output directory if it doesn't exist
output_dir = 'icons'
os.makedirs(output_dir, exist_ok=True)

# Delete all files inside the icons folder except for pictogram.png
if os.path.isdir(output_dir):
    for file_name in os.listdir(output_dir):
        file_path = os.path.join(output_dir, file_name)
        if file_name != 'pictogram.png':
            os.remove(file_path)

# Load the pictogram image
pictogram_path = os.path.join(output_dir, 'pictogram.png')
pictogram_image = Image.open(pictogram_path).convert('RGBA')

# Generate icons for each color
for color_name, color_values in colors.items():
    # Extract RGB values
    r, g, b = color_values

    # Create a solid color image
    image = Image.new('RGB', (250, 250), (r, g, b))

    # Make the color more pastel
    pastel_color = tuple(int(pastel_intensity * channel) for channel in (r, g, b))
    pastel_image = ImageOps.colorize(image.convert('L'), pastel_color, (255, 255, 255))

    # Add a border
    border_color = tuple(int(0.5 * channel) for channel in (r, g, b))
    bordered_image = ImageOps.expand(pastel_image, border=20, fill=border_color)

    # Calculate the maximum size that maintains the aspect ratio of the pictogram
    max_size = int(min(bordered_image.size) * pictogram_scale)

    # Resize the pictogram while maintaining aspect ratio
    pictogram_resized = pictogram_image.copy()
    pictogram_resized.thumbnail((max_size, max_size), Image.ANTIALIAS)

    # Calculate the position of the pictogram
    pictogram_position = ((bordered_image.size[0] - pictogram_resized.width) // 2,
                          (bordered_image.size[1] - pictogram_resized.height) // 2)

    # Paste the pictogram onto the icon
    bordered_image.paste(pictogram_resized, pictogram_position, mask=pictogram_resized)

    # Save the image with the color name as the filename
    filename = f"{color_name}_icon.png"
    file_path = os.path.join(output_dir, filename)
    bordered_image.save(file_path)

    print(f"Generated icon: {filename}")
