# Importación para clases abstractas
from abc import ABC, abstractmethod
# Clase abstracta Servicio
class Servicio(ABC):
    def __init__(self, nombre, tarifa):
        self.nombre = nombre
        self.tarifa = tarifa
    # Getter y setter para nombre
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, valor):
        if not valor or valor.strip() == "":
            raise ValueError("Nombre del servicio no puede estar vacio")
        self._nombre = valor
    # Getter y setter para tarifa
    @property
    def tarifa(self):
        return self._tarifa
    @tarifa.setter
    def tarifa(self, valor):
        if valor <= 0:
            raise ValueError("Tarifa debe ser mayor que cero")
        self._tarifa = valor
    # Método abstracto para calcular costo
    @abstractmethod
    def calcular_costo(self, tiempo):
        pass
    # Método abstracto para descripción
    @abstractmethod
    def descripcion(self):
        pass
# Servicio 1 Reserva de sala
class ReservaSala(Servicio):
    def calcular_costo(self, horas):
        if horas <= 0:
            raise ValueError("Horas invalidas")
        return self.tarifa * horas
    def descripcion(self):
        return "Servicio de reserva de sala por horas"
# Servicio 2 Alquiler de equipos
class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias):
        if dias <= 0:
            raise ValueError("Dias invalidos")
        return self.tarifa * dias
    def descripcion(self):
        return "Servicio de alquiler de equipos por dias"
# Servicio 3 Asesoria especializada
class Asesoria(Servicio):
    def calcular_costo(self, sesiones):
        if sesiones <= 0:
            raise ValueError("Sesiones invalidas")
        # Incluye recargo adicional
        return (self.tarifa * sesiones) * 1.1
    def descripcion(self):
        return "Servicio de asesoria especializada"