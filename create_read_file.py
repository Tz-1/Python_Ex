def crear_archivo():
    try:
        archivo = open("informacion.dat", "x", encoding = "utf-8")
        archivo.write("Datos de información en la línea 1 \nDatos de información en la línea 2 \nDatos de información en la línea 3 \nDatos de información en la línea 4 \nDatos de información en la línea 5")
        archivo.close()
    except FileExistsError:
        print("El archivo informacion.dat existe o a sido creado previamente")
    except Exception as error:
        print("Se ha generado un error no previsto", type(error).__name__)

crear_archivo()

"""
def crear_archivo():
    try:
        with open("informacion.dat", "x", encoding="utf-8") as archivo:
            archivo.write("Datos de información en la línea 1 \nDatos de información en la línea 2 \nDatos de información en la línea 3 \nDatos de información en la línea 4 \nDatos de información en la línea 5")
    except FileExistsError:
        print("El archivo informacion.dat existe o ha sido creado previamente")
    except Exception as error:
        print("Se ha generado un error no previsto:", type(error).__name__)
"""