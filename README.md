# GIF Panelizer 🎞️

Welcome to the fun and exciting world of GIF Panelizer! This Python script takes in PNG images, divides them into quadrants, and then turns them into super cool 4-frame GIFs. It's like magic, but with code! ✨

## How It Works 🛠️

The script works by taking an image URL input along with optional quality and duration parameters. It then creates a GIF by dividing the image into four equal quadrants and using each quadrant as a frame. The processed images are saved to the `PROCESSED` folder, while the newly created GIFs end up in the `GIFS` folder.

Here's a quick overview of the folder structure:

- `PROCESSED`: The script saves the processed image files to this folder.
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

These parameters can be adjusted by providing optional arguments while entering the image URL. Use `--q:QUALITY` and `--d:DURATION` to adjust the quality and duration, respectively.

## Example 🖼️

Here's an example to show you the magic in action!

**Input Image:**

![Input Image 2](https://awardable.s3.amazonaws.com/assets/2.png)

**Output GIF:**

![Output GIF 2](https://awardable.s3.amazonaws.com/assets/2.gif)

## Running the Script 🏃

To run the script, simply execute the Python script:

```bash
python gif_panelizer.py
```

The script will prompt you to enter the image URL along with optional quality and duration parameters.

Example:

```
Enter the image URL and optional arguments: https://imageurl.com/image.png --q:95 --d:500
```

### Optional Arguments
You can provide optional arguments to adjust the quality and duration of the generated GIF:

--q:QUALITY: Sets the quality of the GIF (larger values result in better quality but larger file sizes). Acceptable range: 1 to 100. Default value: 95.

--d:DURATION: Sets the duration between frames in milliseconds (shorter durations result in faster animations). Acceptable range: any positive integer value. Default value: 100.

For example, if you want to create a GIF with a quality of 80 and a duration of 200 milliseconds between frames, you can enter the following:

```
Enter the image URL and optional arguments: https://imageurl.com/image.png --q:80 --d:200
```

Voilà! 🎉 The script processes the image, saves it to the PROCESSED folder, and creates a GIF in the GIFS folder with the specified quality and duration.

Now go on and create some amazing GIFs! 🌟