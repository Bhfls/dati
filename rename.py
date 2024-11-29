import os

def rename_files_in_subdirectories(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == 'mian.py':
                old_file_path = os.path.join(dirpath, filename)
                new_file_path = os.path.join(dirpath, 'main.py')
                os.rename(old_file_path, new_file_path)
                print(f'Renamed {old_file_path} to {new_file_path}')

# 示例用法
root_directory = '/cloudide/workspace/dati'  # 替换为你的根目录路径
rename_files_in_subdirectories(root_directory)