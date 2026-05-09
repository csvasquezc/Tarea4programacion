# Archivo encargado del registro de eventos y errores
from datetime import datetime
def registrar_log(mensaje):
    try:
        # Obtener fecha y hora actual
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Formato del mensaje
        linea = fecha_hora + " " + mensaje + "\n"
        # Escribir en el archivo logs.txt
        with open("logs.txt", "a", encoding="utf-8") as archivo:
            archivo.write(linea)
    except Exception as e:
        # En caso extremo de fallo en el log
        print("Error al escribir en el archivo de logs")
    finally:
        # Se ejecuta siempre
        pass