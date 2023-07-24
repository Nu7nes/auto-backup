import os
import shutil
import sys
from tqdm import tqdm


def print_with_update(item_path):
    line_length = 100  # Define o comprimento da linha que você deseja utilizar

    # Preenche a string com espaços adicionais, se necessário
    item_path_padded = item_path.ljust(line_length)[:line_length]

    # Imprime a linha atualizando o conteúdo anterior
    sys.stdout.write('      Working on --> ' + item_path_padded + '\r')
    sys.stdout.flush()


directory = 'Estudo'
source_directory = f'C:/Users/jessica/Documents/{directory}'
destination_directory = f'D:/{directory}'
folders_to_ignore = ['node_modules', '.git', '.tmp.driveupload', 'venv']


print('     Verifying...')
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)
    print("         >>> Pasta criada com sucesso!")
else:
    print("         >>> A pasta já existe.")



print('     Initializing...')
def copy_files_with_ignore(src, dst, ignore_folders=[]):
    for item  in tqdm(os.listdir(src), desc='   Copying', unit='item'):

        item_path = os.path.join(src, item)
        
        if os.path.isdir(item_path):
            if item in ignore_folders:
                continue
            
            dst_item_path = os.path.join(dst, item)
            os.makedirs(dst_item_path, exist_ok=True)
            copy_files_with_ignore(item_path, dst_item_path, ignore_folders)
        else:
            shutil.copy2(item_path, dst)


copy_files_with_ignore(source_directory, destination_directory, folders_to_ignore)
print(' -----------------------------')
print('     Is ok! Backup ready!')
