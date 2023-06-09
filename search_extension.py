import os
import shutil
while True:
    # Pedir al usuario la extensión a buscar
    extension = input("Enter the file extension to search for (without the dot): ")

    # Obtener el directorio actual
    dir_path = os.getcwd()

    # Crear una carpeta 'busqueda' en el directorio actual
    busqueda_dir = os.path.join(dir_path, 'busqueda')
    if not os.path.exists(busqueda_dir):
        os.makedirs(busqueda_dir)
    print(f"The folder 'search' was created in {dir_path}")
    print(f"Files with the extension .{extension} will be searched for in {dir_path}")
    print(f"The found files will be copied to {busqueda_dir}")
    print("wait...")
    
    # Recorrer todos los archivos del directorio actual
    count = 0
    for root, dirs, files in os.walk(dir_path):
        for filename in files:
            # Si el archivo tiene la extensión buscada, copiarlo a la carpeta 'busqueda'
            if filename.endswith(f".{extension}"):
                if not os.path.exists(os.path.join(busqueda_dir, filename)):
                    shutil.copy2(os.path.join(root, filename), os.path.join(busqueda_dir, filename))
                    print(f"The file {filename} was copied in {busqueda_dir}")
                    count += 1 # Contador de archivos encontrados
                else:
                    print(f"The file {filename} alredy exist in {busqueda_dir}")    
    print("Search finished")
    print(f"Found {count} files with the extension .{extension}")


    respuesta = input("Do you want to perform another search? (y/n):")
    if respuesta.lower() != "y":
        break