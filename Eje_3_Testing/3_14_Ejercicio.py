archivo=input("Ingrese el nombre del archivo: ")
try:
    f=open(archivo, "r")
    contenido=f.read()
    print(contenido)
    f.close()
except FileNotFoundError:
    print("El archivo no existe")
except IOError:
    print("Error de lectura o escritura")
except Exception as e:
    print(f"Ha ocurrido un error:", {e})