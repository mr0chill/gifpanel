import os
import shutil
from PIL import Image

def create_gif_from_quadrants(image_path, output_path):
    img = Image.open(image_path)
    width, height = img.size
    frame_width, frame_height = width // 2, height // 2
    
    frames = [
        img.crop((0, 0, frame_width, frame_height)),
        img.crop((frame_width, 0, width, frame_height)),
        img.crop((0, frame_height, frame_width, height)),
        img.crop((frame_width, frame_height, width, height)),
    ]

    frames[0].save(
        output_path,
        format="GIF",
        save_all=True,
        append_images=frames[1:],
        optimize=True,
        quality=95,
        duration=100,
        loop=0,
    )

input_folder = "IMAGES"
processed_folder = "PROCESSED"
gifs_folder = "GIFS"

if not os.path.exists(processed_folder):
    os.makedirs(processed_folder)

if not os.path.exists(gifs_folder):
    os.makedirs(gifs_folder)

for root, _, files in os.walk(input_folder):
    for file in files:
        if file.lower().endswith(".png"):
            input_path = os.path.join(root, file)
            img = Image.open(input_path)
            
            processed_path = os.path.join(processed_folder, file)
            img.save(processed_path)
            shutil.move(input_path, processed_path)

            gif_output_path = os.path.join(gifs_folder, file.rsplit(".", 1)[0] + ".gif")
            create_gif_from_quadrants(processed_path, gif_output_path)

print("Processing complete.")
