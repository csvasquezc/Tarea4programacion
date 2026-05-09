# Clase Reserva que integra cliente y servicio
from excepciones import ErrorReserva
from logger import registrar_log
class Reserva:
    def __init__(self, cliente, servicio, tiempo):
        self.cliente = cliente
        self.servicio = servicio
        self.tiempo = tiempo
        self.estado = "Pendiente"
    # Método para confirmar reserva
    def confirmar(self):
        self.estado = "Confirmada"
    # Método para cancelar reserva
    def cancelar(self):
        self.estado = "Cancelada"
    # Método principal para procesar la reserva
    def procesar(self):
        try:
            # Validación de datos
            if self.tiempo <= 0:
                raise ErrorReserva("Tiempo de reserva invalido")
            if self.cliente is None:
                raise ErrorReserva("Cliente no definido")
            if self.servicio is None:
                raise ErrorReserva("Servicio no definido")
            # Cálculo del costo usando polimorfismo
            costo = self.servicio.calcular_costo(self.tiempo)
        except ErrorReserva as e:
            registrar_log("Error en reserva " + str(e))
            self.cancelar()
            raise
        except Exception as e:
            registrar_log("Error inesperado " + str(e))
            self.cancelar()
            # Encadenamiento de excepción
            raise ErrorReserva("Fallo al procesar reserva") from e
        else:
            # Se ejecuta si no hay errores
            self.confirmar()
            registrar_log("Reserva procesada correctamente")
            return costo
        finally:
            # Siempre se ejecuta
            registrar_log("Proceso de reserva finalizado")
    # Método para mostrar información
    def mostrar_info(self):
        return f"Reserva de {self.cliente.nombre} estado {self.estado}"