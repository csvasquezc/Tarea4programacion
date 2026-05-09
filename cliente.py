# Clase base abstracta para entidades del sistema
from abc import ABC, abstractmethod

class Entidad(ABC):
    def __init__(self, id):
        self._id = id  # atributo protegido

    @abstractmethod
    def mostrar_info(self):
        pass


# Clase Cliente con encapsulación y validaciones
class Cliente(Entidad):

    def __init__(self, id, nombre, email):
        super().__init__(id)
        self.nombre = nombre
        self.email = email  # se valida con el setter

    # Getter para el id
    @property
    def id(self):
        return self._id

    # Getter y setter para nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        # Validación básica
        if not valor or valor.strip() == "":
            raise ValueError("Nombre no puede estar vacio")
        self._nombre = valor

    # Getter y setter para email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        # Validación simple de email
        if "@" not in valor or "." not in valor:
            raise ValueError("Email invalido")
        self._email = valor

    # Método obligatorio heredado de la clase abstracta
    def mostrar_info(self):
        return f"Cliente {self.nombre} con email {self.email}"