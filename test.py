import os

def print_file_paths(directory):
    """
    Print the paths of all files within the given directory.

    Args:
        directory (str): The directory path to search.
    """
    # Iterate over all files and directories within the given directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Construct the full path to the file
            file_path = os.path.join(root, file)
            # Print the file path       
            print(file_path)

# Example usage:
directory_path = r"D:\Projects\Splitter\app\Splitterapp\Testing\parts"
print_file_paths(directory_path)
