import os
import json

with open('colors.json') as file:
    colors_dict = json.load(file)
    color_names = list(colors_dict.keys())

# Create the bat_triggers folder if it doesn't exist
if not os.path.exists("bat_triggers"):
    os.makedirs("bat_triggers")

# Get the grandparent directory of the script
grandparent_directory = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# Generate batch files
for color in color_names:
    file_name = f"setlights_{color}.bat"
    file_path = os.path.join("bat_triggers", file_name)

    with open(file_path, "w") as file:
        file.write(f'@echo off\n')
        file.write(f'cd /d "{grandparent_directory}"\n')
        file.write(f'python set_studio_to.py {color}')

    print(f"Generated batch file: {file_name}")