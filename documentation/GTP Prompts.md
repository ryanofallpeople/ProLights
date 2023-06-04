# Icon Generator


## Initial Prompt
Write a python script to generate numerous 250x250 pixel icons filled with a solid color.

The script will take a JSON file named `colors.json` as an input
colors.json is a dictionary with string names of colors as the key. Each key's value is a three item array that contains the corresponding R, G, and B values.

For each item in the dictionary generate an image file with a solid color that matches the color values in the array. 

the output of the script should be a folder at `/icons` containing all of the generated icons.

The naming convention for each output file is as follows: `<color>_icon.png`

Use the OS library file paths

---
## Revision

For each icon make the colors more pastel and add a 20px border around the edge in a darker shade of the color

Factor out a variable for how intense the pastel effect should be and put it at the top of the script.

Add a pictogram to the center of the icon with a factored out variable for the scale factor.

The pictogram will come in the form of a png file that will need to be scaled to 50%. Make sure the alpha channel is supported.

Use the png named `./icons/pictogram.png`

Ensure that the aspect ratio of the pictogram isn't affected by any scaling.




