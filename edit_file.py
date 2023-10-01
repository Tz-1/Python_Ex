def editar_lineas(old, new):
    try:
        with open("informacion.dat", "r", encoding="utf-8") as archivo:
            remplazo = ""
            for linea in archivo:
                linea = linea.strip()
                cambios = linea.replace(old, new)
                remplazo = remplazo + cambios + "\n"

        with open("informacion.dat", "w", encoding="utf-8") as archivo:
            archivo.write(remplazo)

    except FileNotFoundError:
        print("No se encuentra el archivo")
    except Exception as error:
        print('Se ha generado un error no previsto',type(error).__name__)
    finally:
        print("Se ha editado")

editar_lineas("información", "Procesamiento")