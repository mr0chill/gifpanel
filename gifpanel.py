import os
import re
import requests
from PIL import Image
from io import BytesIO
import time

def create_gif_from_quadrants(image, output_path, quality, duration, upscale_factor):
    width, height = image.size
    frame_width, frame_height = width // 2, height // 2

    frames = [
        image.crop((0, 0, frame_width, frame_height)).resize((frame_width * upscale_factor, frame_height * upscale_factor)),
        image.crop((frame_width, 0, width, frame_height)).resize((frame_width * upscale_factor, frame_height * upscale_factor)),
        image.crop((0, frame_height, frame_width, height)).resize((frame_width * upscale_factor, frame_height * upscale_factor)),
        image.crop((frame_width, frame_height, width, height)).resize((frame_width * upscale_factor, frame_height * upscale_factor)),
    ]

    frames[0].save(
        output_path,
        format="GIF",
        save_all=True,
        append_images=frames[1:],
        optimize=True,
        quality=quality,
        duration=duration,
        loop=0,
    )

def process_image():
    processed_folder = "PROCESSED"
    gifs_folder = "GIFS"

    if not os.path.exists(processed_folder):
        os.makedirs(processed_folder)

    if not os.path.exists(gifs_folder):
        os.makedirs(gifs_folder)

    input_text = input("Enter the image URL and optional arguments: ")

    quality = 95
    duration = 100
    upscale_factor = 2

    quality_arg = re.search(r"--q:(\d+)", input_text)
    if quality_arg:
        quality = int(quality_arg.group(1))

    duration_arg = re.search(r"--d:(\d+)", input_text)
    if duration_arg:
        duration = int(duration_arg.group(1))

    upscale_arg = re.search(r"--u:(\d+)", input_text)
    if upscale_arg:
        upscale_factor = int(upscale_arg.group(1))

    image_url = re.sub(r"\s*--q:\d+|--d:\d+|--u:\d+", "", input_text)

    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    filename = os.path.basename(image_url)
    file_extension = os.path.splitext(filename)[1]
    processed_path = os.path.join(processed_folder, filename)
    image.save(processed_path, format=file_extension[1:])

    gif_output_path = os.path.join(gifs_folder, filename.rsplit(".", 1)[0] + ".gif")
    create_gif_from_quadrants(image, gif_output_path, quality, duration, upscale_factor)

    print("Processing complete.")


def main():
    while True:
        process_image()
        timeout = 180  # 3 minutes timeout in seconds
        print(f"Do you want to create another GIF?")
        start_time = time.time()

        while time.time() - start_time < timeout:
            answer = input()
            if answer.lower() in ['', 'y', 'yes']:
                break
            elif answer.lower() in ['n', 'no', 'nah']:
                return
            time.sleep(0.1)

if __name__ == "__main__":
    main()
