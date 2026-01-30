import os
import subprocess

def list_files(directory_path, recursive=False):
    """
    List all files in the given directory.
    
    :param directory_path: Path to the directory
    :param recursive: If True, list files in subdirectories as well
    :return: List of file paths
    """
    files_list = []

    #Validate directory path
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory '{directory_path}' does not exist.")
    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"'{directory_path} is not a directory.")
    
    if recursive:
        # Walk through directory tree
        for root, _, files in os.walk(directory_path):
            for file in files:
                files_list.append(os.path.join(root, file))
    
    else:
        # List only files in the given directory
        for entry in os.listdir(directory_path):
            full_path = os.path.join(directory_path, entry)
            if os.path.isfile(full_path):
                files_list.append(full_path)
    
    return files_list

if __name__ == "__main__":
    
    dwebp_path = ".\\dwebp.exe"

    try:
        path = input("Enter directory path: ").strip()
        recursive_choice = input("List files recursively? (y/n): ").strip().lower() == 'y'

        files = list_files(path, recursive_choice)
        
        if files:
            for file_path in files:
                file_name = file_path[len(path)+1:-5]
                new_file_path = f".\\output\\{file_name}.png"
                # print(f"Calling: {dwebp_path}, {file_path}, -o {new_file_path}")
                # subprocess.run([dwebp_path, f"\"file_path\"", "-o" f"\"{new_file_path}\""])
                subprocess.run(f"{dwebp_path} \"{file_path}\" -o \"{new_file_path}\"")
                # print(f"Processed {file_name}")               
        else:
            print("No files found in the directory.")
        
    except (FileNotFoundError, NotADirectoryError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")