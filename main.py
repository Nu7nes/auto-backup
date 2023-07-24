import os
import shutil

directory = 'Estudo'
source_directory = f'C:/Users/jessica/Documents/{directory}'
destination_directory = f'D:/{directory}'
folders_to_ignore = ['node_modules', '.git', '.tmp.driveupload']

print('     Verifying...')
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)
    print("         >>> Pasta criada com sucesso!")
else:
    print("         >>> A pasta já existe.")

print('     Initializing...')
def copy_files_with_ignore(src, dst, ignore_folders=[]):

    for item  in os.listdir(src):
        item_path = os.path.join(src, item)
        if os.path.isdir(item_path):
            if item in ignore_folders:
                continue
            
            dst_item_path = os.path.join(dst, item)
            os.makedirs(dst_item_path, exist_ok=True)
            copy_files_with_ignore(item_path, dst_item_path, ignore_folders)
        else:
            print('             Copying --> ',item_path, end='\r')
            shutil.copy2(item_path, dst)

copy_files_with_ignore(source_directory, destination_directory, folders_to_ignore)
print(' -----------------------------')
print('     Is ok! Backup ready!')
