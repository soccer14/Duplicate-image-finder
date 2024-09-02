# duplicate finder from photo in Desktop folder

# This programe is simple and helps clear Photo folder of duplicate images to save space.
# 1) create a folder in your desktop
# 2) Drag and drop photos into the folder (only Photos will work)

import os
import hashlib
from PIL import Image

def calculate_hash(image_path):
    """this calculate hash for the image file."""
    with Image.open(image_path) as img:
        img = img.convert('RGB')  # Ensure consistent format
        return hashlib.md5(img.tobytes()).hexdigest()

def find_duplicates(folder_path):
    """Find and move duplicate images to a 'duplicates' folder."""
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return

    duplicates_folder = os.path.join(folder_path, "duplicates")
    os.makedirs(duplicates_folder, exist_ok=True)

    image_hashes = {}
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                file_path = os.path.join(root, file)
                file_hash = calculate_hash(file_path)
                
                if file_hash in image_hashes:
                    # Move duplicate to the duplicates folder
                    duplicate_path = os.path.join(duplicates_folder, file)
                    os.rename(file_path, duplicate_path)
                    print(f"Moved duplicate: {file_path} to {duplicate_path}")
                else:
                    image_hashes[file_hash] = file_path

    print("Processing complete.")

# Example usage
folder_to_process = "/Users/live/Desktop/images"
find_duplicates(folder_to_process)
