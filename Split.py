import os
import zipfile
import math

def split_file(input_file, chunk_size):
    with open(input_file, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk

def create_parts_directory(input_folder):
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)

# def create_parts(input_folder):
#     file_name = os.path.basename(input_folder)
#     print("Entered create parts function")
#     print(file_name)
#     zip_file_path = os.path.join(input_folder,'parts', file_name + '.zip')
#     print("Zip file path is: ",zip_file_path)
#     with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
#         for root, _, files in os.walk(input_folder):
#             for file in files:
#                 file_path = os.path.join(root, file)
#                 zipf.write(file_path, os.path.relpath(file_path, input_folder))

#     # Split the zip file into parts
#     total_size = os.path.getsize(zip_file_path)
#     chunk_size = 100 * 1024 * 1024  # 100MB
#     num_parts = math.ceil(total_size / chunk_size)
#     print("Line 34")
#     with open(zip_file_path, 'rb') as f_in:
#         for i in range(num_parts):
#             with open(f'parts/{file_name}_part{i+1}.bin', 'wb') as f_out:
#                 f_out.write(f_in.read(chunk_size))

def create_parts(input_folder):
    file_name = os.path.basename(input_folder)
    print("Entered create parts function")
    print(file_name)
    zip_file_path = os.path.join(input_folder, 'parts', file_name + '.zip')
    print("Zip file path is: ", zip_file_path)
    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(input_folder):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, input_folder))

    # Split the zip file into parts
    total_size = os.path.getsize(zip_file_path)
    if total_size == 0:
        print("Error: Zip file is empty.")
        return

    chunk_size = 100 * 1024 * 1024  # 100MB
    num_parts = math.ceil(total_size / chunk_size)
    # print("Line 34")
    with open(zip_file_path, 'rb') as f_in:
        for i in range(num_parts):
            with open(os.path.join(input_folder, 'parts', f'{file_name}_part{i+1}.bin'), 'wb') as f_out:
                f_out.write(f_in.read(chunk_size))

def zip_directory(directory_path):
    base_dir = os.path.basename(directory_path)
    parts_dir = os.path.join(directory_path, "parts")
    os.makedirs(parts_dir, exist_ok=True)
    zip_filename = os.path.join(parts_dir, base_dir + ".zip")
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, directory_path)
                zipf.write(file_path, arcname=arcname)

    print(f"Directory '{directory_path}' has been zipped to '{zip_filename}'")

def delete_zip_file(zip_file_path):
    try:
        if os.path.exists(zip_file_path) and zip_file_path.endswith('.zip'):
            os.remove(zip_file_path)
            print(f"Deleted {zip_file_path} successfully.")
        else:
            print(f"The file {zip_file_path} does not exist or is not a ZIP file.")
    except Exception as e:
        print(f"An error occurred: {e}")


def start_split(input_folder):
    print("Receiver in Split.py")
    print("The received input directory is ", input_folder)
    zip_directory(input_folder)
    # create_parts_directory(input_folder)
    create_parts(input_folder)
    print("Folder has been zipped and split into parts successfully.")
    file_name = os.path.basename(input_folder)
    print("Here")
    print(f'{input_folder}\parts\{file_name}.zip')
    delete_zip_file(f'{input_folder}\parts\{file_name}.zip')
