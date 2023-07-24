# import os
# from shutil import make_archive


# files = os.listdir(source)
# print(files)

# os.rename('teste.txt', "teste/teste.txt") # mover arquivos
# shutil.copy2('teste.txt', 'teste/teste.txt') # copiar arquivos
# make_archive('backup', 'zip', source) # compactar arquivos

# for arquivo in files:
#     if "Estudo" in arquivo:
#         make_archive('backup_estudos', 'zip', arquivo)

import os
import shutil

directory = 'Estudo'
source_directory = f'C:/Users/jessica/Documents/{directory}'
destination_directory = f'D:/{directory}'
folders_to_ignore = ['node_modules', '.git', '.tmp.driveupload']

# Verifica se a pasta existe
if not os.path.exists(destination_directory):
    # Cria a pasta se ela não existir
    os.makedirs(destination_directory)
    print("Pasta criada com sucesso!")
else:
    print("A pasta já existe.")


def copy_files_with_ignore(src, dst, ignore_folders=[]):
    for item in os.listdir(src):
        item_path = os.path.join(src, item)
        if os.path.isdir(item_path):
            # Se for uma pasta e estiver na lista de pastas a serem ignoradas, pule para a próxima iteração
            if item in ignore_folders:
                continue
            # Cria a pasta de destino se ainda não existir
            dst_item_path = os.path.join(dst, item)
            os.makedirs(dst_item_path, exist_ok=True)
            # Chama recursivamente a função para copiar os arquivos dentro da pasta
            copy_files_with_ignore(item_path, dst_item_path, ignore_folders)
        else:
            # Se for um arquivo, copie-o
            shutil.copy2(item_path, dst)



# Copia os arquivos e pastas, ignorando as pastas especificadas
copy_files_with_ignore(source_directory, destination_directory, folders_to_ignore)
