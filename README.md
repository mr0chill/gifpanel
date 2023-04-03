# GIF Panelizer 🎞️

Welcome to the fun and exciting world of GIF Panelizer! This Python script takes in PNG images, divides them into quadrants, and then turns them into super cool 4-frame GIFs. It's like magic, but with code! ✨

## How It Works 🛠️

The script works by scanning the `IMAGES` folder for PNG files. For each image, it creates a GIF by dividing the image into four equal quadrants and using each quadrant as a frame. The processed images are then moved to the `PROCESSED` folder, while the newly created GIFs end up in the `GIFS` folder.

Here's a quick overview of the folder structure:

- `IMAGES`: Put your input PNG files here.
- `PROCESSED`: The script moves processed PNG files to this folder.
- `GIFS`: The script saves the generated GIFs in this folder.

## Examples 🖼️

Here are some examples to show you the magic in action!

### Example 1

**Input Image:**

![Input Image 1](example1_input.png)

**Output GIF:**

![Output GIF 1](example1_output.gif)

### Example 2

**Input Image:**

![Input Image 2](example2_input.png)

**Output GIF:**

![Output GIF 2](example2_output.gif)

## Running the Script 🏃

To run the script, simply put your PNG images in the `IMAGES` folder and then execute the Python script:

```bash
python gif_panelizer.py
```

Voilà! 🎉 The script processes the images, moves them to the PROCESSED folder, and creates GIFs in the GIFS folder.

Now go on and create some amazing GIFs! 🌟
