import os
import random
import shutil

def get_random_tux():
    source_dir = "images"
    output_dir = "output"
    output_filename = "img.png"
    output_path = os.path.join(output_dir, output_filename)

    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    os.makedirs(output_dir, exist_ok=True)

    images = [f for f in os.listdir(source_dir) if f.lower().endswith('.png')]

    if not images:
        print(f"Error: No PNG images found in '{source_dir}'.")
        return

    random_image = random.choice(images)
    source_path = os.path.join(source_dir, random_image)

    try:
        shutil.copy2(source_path, output_path)
        print(f"Success! '{random_image}' copied to '{output_path}'.")
    except Exception as e:
        print(f"An error occurred while copying: {e}")

if __name__ == "__main__":
    get_random_tux()
