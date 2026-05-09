# Archivo de excepciones personalizadas del sistema
# Clase base para errores del sistema
class ErrorSistema(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
# Error relacionado con clientes
class ErrorCliente(ErrorSistema):
    def __init__(self, mensaje="Error en cliente"):
        super().__init__(mensaje)
# Error relacionado con servicios
class ErrorServicio(ErrorSistema):
    def __init__(self, mensaje="Error en servicio"):
        super().__init__(mensaje)
# Error relacionado con reservas
class ErrorReserva(ErrorSistema):
    def __init__(self, mensaje="Error en reserva"):
        super().__init__(mensaje)