import os
import zipfile
import rarfile
import py7zr
import re

IMAGE_EXTENSIONS = ('.png', '.jpg', '.bmp', '.gif')
ARCHIVE_EXTENSIONS = ('.zip', '.rar', '.7z')

def sanitize_filename(filename):
    # Remove any invalid characters from the filename
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def extract_images_from_zip(file_path, output_dir):
    print(f"Processing ZIP file: {file_path}")
    try:
        with zipfile.ZipFile(file_path, 'r') as z:
            extract_images(z, file_path, output_dir)
    except zipfile.BadZipFile:
        print(f"Skipping invalid ZIP file: {file_path}")
    except Exception as e:
        print(f"Error processing ZIP file {file_path}: {e}")

def extract_images_from_rar(file_path, output_dir):
    print(f"Processing RAR file: {file_path}")
    try:
        with rarfile.RarFile(file_path, 'r') as r:
            extract_images(r, file_path, output_dir)
    except rarfile.RarCannotExec:
        print(f"Cannot extract {file_path}: 'unrar' utility not found. Please install 'unrar'.")
    except rarfile.BadRarFile:
        print(f"Skipping invalid RAR file: {file_path}")
    except Exception as e:
        print(f"Error processing RAR file {file_path}: {e}")

def extract_images_from_7z(file_path, output_dir):
    print(f"Processing 7Z file: {file_path}")
    try:
        with py7zr.SevenZipFile(file_path, 'r') as z:
            extract_images_7z(z, file_path, output_dir)
    except py7zr.Bad7zFile:
        print(f"Skipping invalid 7Z file: {file_path}")
    except Exception as e:
        print(f"Error processing 7Z file {file_path}: {e}")

def extract_images(archive, file_path, output_dir):
    count = 1
    base_name = sanitize_filename(os.path.splitext(os.path.basename(file_path))[0])
    for file_info in archive.infolist():
        if file_info.filename.lower().endswith(IMAGE_EXTENSIONS):
            ext = os.path.splitext(file_info.filename)[1]
            new_name = f"{base_name}{count:02d}{ext}"
            extract_path = os.path.join(output_dir, sanitize_filename(new_name))
            print(f"Extracting {file_info.filename} to {extract_path}")
            try:
                with archive.open(file_info) as source, open(extract_path, 'wb') as target:
                    target.write(source.read())
                count += 1
            except Exception as e:
                print(f"Error extracting {file_info.filename}: {e}")

def extract_images_7z(archive, file_path, output_dir):
    count = 1
    base_name = sanitize_filename(os.path.splitext(os.path.basename(file_path))[0])
    for filename in archive.getnames():
        if filename.lower().endswith(IMAGE_EXTENSIONS):
            ext = os.path.splitext(filename)[1]
            new_name = f"{base_name}{count:02d}{ext}"
            extract_path = os.path.join(output_dir, sanitize_filename(new_name))
            print(f"Extracting {filename} to {extract_path}")
            try:
                with archive.open(filename) as source, open(extract_path, 'wb') as target:
                    target.write(source.read())
                count += 1
            except Exception as e:
                print(f"Error extracting {filename}: {e}")

def main(directory_path, output_dir):
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                if file_path.lower().endswith('.zip'):
                    extract_images_from_zip(file_path, output_dir)
                elif file_path.lower().endswith('.rar'):
                    extract_images_from_rar(file_path, output_dir)
                elif file_path.lower().endswith('.7z'):
                    extract_images_from_7z(file_path, output_dir)
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

if __name__ == "__main__":
    try:
        directory_path = input("Enter the directory path to search for archives: ")
        output_dir = input("Enter the directory path to save extracted images: ")
        os.makedirs(output_dir, exist_ok=True)
        main(directory_path, output_dir)
    except Exception as e:
        print(f"Error: {e}")
