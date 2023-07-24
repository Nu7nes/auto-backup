import os
import shutil

source = 'C:/Users/jessica/Documents/Estudo'
destination = ''

files = os.listdir()
print(files)

# os.rename('teste.txt', "teste/teste.txt")
# shutil.copy2('teste.txt', 'teste/teste.txt')
shutil.make_archive('backup', 'zip', 'teste')
