import os
import shutil

def check_directory(directory : str) -> bool:
    if (os.path.exists(directory)):
        return True
    return False

def split_file(path : str):
    return os.path.splitext(os.path.basename(path))

def move_file(source_path : str, destination_path : str):
    try:
        print(f"File moved successfully from {source_path} to {destination_path}")
        shutil.move(source_path, destination_path)
    except Exception as e:
        print(f"Error moving file: {e}")

def main():
    path = 'C:/Users/naemwear/Downloads'
    files_list = os.listdir(path)
    
    for file in files_list:
        current_path = f'{path}/{file}'
        file_type = split_file(current_path)[-1]
        destination_path = f'{path}/{file_type}'
        
        if (file_type is not None and file_type is not ''):
            if (check_directory(destination_path)):
                move_file(current_path, destination_path)
            else:
                os.mkdir(destination_path)
                print(f'Making directory {destination_path}...')
                move_file(current_path, destination_path)
    

if __name__ == '__main__':
    main()