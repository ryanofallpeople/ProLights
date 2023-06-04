from Modules.color_utils import get_rgb as rgb
from Modules.lights_wrapper import studio_obj
import sys
import json

s = studio_obj()
provided_color = sys.argv[1]

# Load the colors dictionary from colors.json
with open('colors.json') as file:
    colors_dict = json.load(file)
    color_names = list(colors_dict.keys())

def arg_validator():
    if(provided_color not in color_names):
        error_msg = f"Invalid color: {provided_color}. Available colors: {', '.join(color_names)}"
        raise ValueError(error_msg)

arg_validator()

s.set_studio(rgb(provided_color))
#s.set_light('STUDIO-FRONT-2', rgb('steel_blue'), 100)