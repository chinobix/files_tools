import os

def renombrar_archivos(directorio):
    # Obtener la lista de archivos en el directorio
    archivos = os.listdir(directorio)
    
    # Contador para los nombres de archivo
    contador = 0
    
    for archivo in archivos:
        if archivo == "rename_files_0000.py":
            continue
        # Construir el nuevo nombre de archivo con cuatro dígitos
        nuevo_nombre = f"{contador:04d}" + os.path.splitext(archivo)[1]
        
        # Ruta completa del archivo antiguo y nuevo
        ruta_antiguo = os.path.join(directorio, archivo)
        ruta_nuevo = os.path.join(directorio, nuevo_nombre)
        
        # Renombrar el archivo
        os.rename(ruta_antiguo, ruta_nuevo)
        
        # Mostrar en pantalla el archivo que se está renombrando
        print(f"Renombrando: {ruta_antiguo} -> {ruta_nuevo}")
        
        # Incrementar el contador
        contador += 1

# Obtener el directorio actual del script
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Llama a la función para renombrar archivos en el directorio actual
renombrar_archivos(directorio_actual)

print("Archivos renombrados con éxito")
print("Presione una tecla para continuar...")
input()
