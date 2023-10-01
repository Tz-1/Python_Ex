def agregar_lineas():
    try:
        archivo = open("informacion.dat", "a", encoding="utf-8")
        archivo.write("\nHola Mundo \nEste en una nueva línea en el archivo \nagregando la segunda línea del archivo \nfinalizando la línea agregada")
        archivo.close()
    except FileNotFoundError:
        print("No se encuentra el archivo informacion.dat")
    except Exception as error:
        print("Se ha generado un error no previsto", type(error).__name__)

agregar_lineas()

"""
def agregar_lineas():
    try:
        with open("informacion.dat", "a", encoding="utf-8") as archivo:
        archivo.write("\nHola Mundo \nEste en una nueva línea en el archivo \nagregando la segunda línea del archivo \nfinalizando la línea agregada")
    except FileNotFoundError:
        print("No se encuentra el archivo informacion.dat")
    except Exception as error:
        print("Se ha generado un error no previsto", type(error).__name__)

agregar_lineas()
"""