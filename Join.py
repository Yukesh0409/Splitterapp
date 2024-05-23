import os
import zipfile

def join_parts(input_folder):
    parts_dir = os.path.join(input_folder, 'parts')
    output_zip_path = os.path.join(input_folder, 'joined.zip')

    # Join binary parts into a single zip file
    with open(output_zip_path, 'wb') as f_out:
        for part_file in sorted(os.listdir(parts_dir)):
            part_path = os.path.join(parts_dir, part_file)
            with open(part_path, 'rb') as f_in:
                f_out.write(f_in.read())

    # Extract the contents of the zip file
    output_folder = os.path.join(input_folder, 'extracted')
    with zipfile.ZipFile(output_zip_path, 'r') as zip_ref:
        zip_ref.extractall(output_folder)

    # Clean up temporary zip file
    os.remove(output_zip_path)

def Join(download_location):
    input_folder = download_location
    join_parts(input_folder)
    print("Parts have been joined and extracted successfully.")
