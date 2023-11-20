import os
import shutil

#input("Presiona Enter para comenzar...")
# Obtener el directorio actual
dir_path = os.getcwd()
archivos = []
directorios = []
extensiones = []
# Obtener la lista de archivos en el directorio
#files = os.listdir(dir_path)
files = [file for file in os.listdir(dir_path) if file != "plex_movie_folder.py"] # lista de archivos sin el archivo actual

#separar archivos de directorios

for file in files:
    if os.path.isfile(file):
        nombre, extension = os.path.splitext(file)
        print(f"{file} -> {nombre}")
        archivos.append(nombre)
        extensiones.append(extension)
    else:
        directorios.append(file)

# hacer directorios con la lista de archivos
for archivo in archivos:
     if not os.path.exists(archivo): # checa si existe el directorio
        os.mkdir(archivo)
        print(archivo + ' folder created')

# mover los archivos a sus respectivos directorios

for file in files:
    if os.path.isfile(file):
        origen = os.path.join(dir_path, file)
        directorio, extension = os.path.splitext(file)
        destino = os.path.join(dir_path, directorio)
        print(f"origen: {origen}")
        print(f"destino: {destino}")
        shutil.move(origen, destino)
        print(f"{archivo + extension} movido a {archivo} folder")


input("Presiona Enter para salir...")
