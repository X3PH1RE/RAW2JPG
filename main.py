from PIL import Image
import os

def convert_raw_to_jpg(raw_file_path, output_directory):
    try:
        with Image.open(raw_file_path) as img:
            img = img.convert("RGB")
            
            base_name = os.path.basename(raw_file_path)
            file_name, _ = os.path.splitext(base_name)
            output_file_path = os.path.join(output_directory, file_name + '.jpg')
            
            img.save(output_file_path, 'JPEG')
            
            print(f"Converted {raw_file_path} to {output_file_path}")
    except Exception as e:
        print(f"Failed to convert {raw_file_path}: {e}")

def convert_directory(raw_directory, output_directory):
    os.makedirs(output_directory, exist_ok=True)
    
    for file_name in os.listdir(raw_directory):
        raw_file_path = os.path.join(raw_directory, file_name)
        if os.path.isfile(raw_file_path):
            convert_raw_to_jpg(raw_file_path, output_directory)

raw_directory = './raw images'
output_directory = './converted'

convert_directory(raw_directory, output_directory)
