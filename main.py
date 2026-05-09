
# Importación de módulos del sistema
from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva
from logger import registrar_log

# Listas para almacenar datos en memoria
clientes = []
reservas = []

print("Inicio del sistema Software FJ")

# Registro de clientes

try:
    c1 = Cliente(1, "Juan", "juan@email.com")
    clientes.append(c1)
    print("Cliente registrado correctamente")
except Exception as e:
    registrar_log(str(e))
    print("Error al registrar cliente")

try:
    # Este cliente generará error por email inválido
    c2 = Cliente(2, "Ana", "correo_invalido")
    clientes.append(c2)
    print("Cliente registrado correctamente")
except Exception as e:
    registrar_log(str(e))
    print("Error al registrar cliente")
# Creación de servicios
try:
    sala = ReservaSala("Sala VIP", 50000)
    equipo = AlquilerEquipo("Laptop", 30000)
    asesoria = Asesoria("Python", 80000)
    print("Servicios creados correctamente")
except Exception as e:
    registrar_log(str(e))
    print("Error al crear servicios")
# Creación de reservas
try:
    r1 = Reserva(c1, sala, 2)
    costo = r1.procesar()
    reservas.append(r1)
    print("Reserva procesada")
    print("Costo de la reserva", costo)
except Exception as e:
    registrar_log(str(e))
    print("Error en reserva")
try:
    # Esta reserva generará error por tiempo inválido
    r2 = Reserva(c1, asesoria, -1)
    costo = r2.procesar()
    reservas.append(r2)
    print("Reserva procesada")
    print("Costo de la reserva", costo)
except Exception as e:
    registrar_log(str(e))
    print("Error en reserva")
# Estado final del sistema
print("Total de clientes registrados", len(clientes))
print("Total de reservas realizadas", len(reservas))
print("Sistema finalizado correctamente")