import os
import shutil

source = 'C:/Users/jessica/Documents/Estudo'
destination = 'D:/'

files = os.listdir()
print(files)

# os.rename('teste.txt', "teste/teste.txt") mover arquivos
# shutil.copy2('teste.txt', 'teste/teste.txt') copiar arquivos
# shutil.make_archive('backup', 'zip', 'teste') compactar arquivos




