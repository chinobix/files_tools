##read files on this folder

import os

# Obtener el directorio actual
dir_path = os.getcwd()

# Obtener la lista de archivos en el directorio
files = os.listdir(dir_path)

#inicializar listas archivos y directorios
archivos = []
directorios = []

#separar archivos de directorios

for file in files:
    if os.path.isfile(file):
        archivos.append(file)
    else:
        directorios.append(file)

# guardar archivo txt
with open('list_files_and_folders.txt', 'w') as f:
    f.write('Directorios: \n')
    for item in directorios:
        f.write(item + '\n')
    f.write('\nArchivos: \n')
    for item in archivos:
        f.write(item + '\n')
#cerrar archivo
f.close()
