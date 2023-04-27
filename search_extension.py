import os
import shutil
while True:
    # Pedir al usuario la extensión a buscar
    extension = input("Introduzca la extensión de archivo a buscar (sin punto): ")

    # Obtener el directorio actual
    dir_path = os.getcwd()

    # Crear una carpeta 'busqueda' en el directorio actual
    busqueda_dir = os.path.join(dir_path, 'busqueda')
    if not os.path.exists(busqueda_dir):
        os.makedirs(busqueda_dir)
    print(f"Se creó la carpeta 'busqueda' en {dir_path}")
    print(f"Se buscarán archivos con la extensión .{extension} en {dir_path}")
    print(f"Los archivos encontrados se copiarán en {busqueda_dir}")
    print("Espere...")
    
    # Recorrer todos los archivos del directorio actual
    count = 0
    for root, dirs, files in os.walk(dir_path):
        for filename in files:
            # Si el archivo tiene la extensión buscada, copiarlo a la carpeta 'busqueda'
            if filename.endswith(f".{extension}"):
                if not os.path.exists(os.path.join(busqueda_dir, filename)):
                    shutil.copy2(os.path.join(root, filename), os.path.join(busqueda_dir, filename))
                    print(f"Se copió el archivo {filename} en {busqueda_dir}")
                    count += 1 # Contador de archivos encontrados
                else:
                    print(f"El archivo {filename} ya existe en {busqueda_dir}")    
    print("Búsqueda finalizada")
    print(f"Se encontraron {count} archivos con la extensión .{extension}")


    respuesta = input("¿Desea realizar otra búsqueda? (s/n): ")
    if respuesta.lower() != "s":
        break