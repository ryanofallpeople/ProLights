import json
import os

def get_rgb(color_name):
    file_path = os.path.join(os.path.dirname(__file__), "../colors.json")
    with open(file_path) as file:
        color_dict = json.load(file)

    default_color = color_dict.get("default", [255, 255, 255])
    return color_dict.get(color_name, default_color)