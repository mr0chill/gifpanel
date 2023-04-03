# GIF Panelizer 🎞️

Welcome to the fun and exciting world of GIF Panelizer! This Python script takes in PNG images, divides them into quadrants, and then turns them into super cool 4-frame GIFs. It's like magic, but with code! ✨

## How It Works 🛠️

The script works by scanning the `IMAGES` folder for PNG files. For each image, it creates a GIF by dividing the image into four equal quadrants and using each quadrant as a frame. The processed images are then moved to the `PROCESSED` folder, while the newly created GIFs end up in the `GIFS` folder.

Here's a quick overview of the folder structure:

- `IMAGES`: Put your input PNG files here.
- `PROCESSED`: The script moves processed PNG files to this folder.
- `GIFS`: The script saves the generated GIFs in this folder.

## GIF Parameters 🎛️

The GIF is created using the following parameters:

- `format="GIF"`: Specifies the output format as a GIF.
- `save_all=True`: Saves all the frames in the sequence as a single file.
- `append_images=frames[1:]`: Appends the remaining frames to the first frame.
- `optimize=True`: Optimizes the GIF for a smaller file size.
- `quality=95`: Sets the quality of the GIF (larger values result in better quality but larger file sizes).
- `duration=100`: Sets the duration between frames in milliseconds (in this case, 100 ms or 10 fps).
- `loop=0`: Sets the number of times the GIF loops (0 means it will loop indefinitely).

These parameters can be adjusted to change the output GIF's appearance and behavior.


## Example 🖼️

Here's an example to show you the magic in action!

**Input Image:**

![Input Image 2](https://awardable.s3.amazonaws.com/assets/2.png)

**Output GIF:**

![Output GIF 2](https://awardable.s3.amazonaws.com/assets/2.gif)

## Running the Script 🏃

To run the script, simply put your PNG images in the `IMAGES` folder and then execute the Python script:

```bash
python gif_panelizer.py
```

Voilà! 🎉 The script processes the images, moves them to the PROCESSED folder, and creates GIFs in the GIFS folder.

Now go on and create some amazing GIFs! 🌟
