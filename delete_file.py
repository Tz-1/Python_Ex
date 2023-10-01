def eliminar_datos_archivo():
    try:
        archivo = open('datos.cvs', 'w')
        archivo.close()
    except FileNotFoundError:
        print('No se encuentra el archivo datos.cvs')
    except Exception as error:
        print('Se ha generado un error no previsto', type(error).__name__)
    finally:
        print("Se ha eliminado todos los datos del archivo exitosamente")

eliminar_datos_archivo()

#Si quieres comprobar si un archivo se puede leer, usa el método readable(), que devolverá True o False.
#archivo.readable()

# Abre un archivo
foo = open('foo.txt', 'wb') # Abrimos el archivo llamado foo.txt en modo escritura binaria
print('Nombre del archivo: ', foo.name)
print('Cerrado o no: ', foo.closed)
print('Modo de acceso: ', foo.mode)