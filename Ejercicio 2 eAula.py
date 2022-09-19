# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 21:50:23 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""
# Declaramos las variables de ambos países, dejando el país "A" con una población menor al B
paisA = 10000
paisB = 15000

# Inicializamos la variable "año" con valor 1 ya que el valor declarado de ambos países es a partir del año 1
año = 1

# Calculamos cuál es el crecimiento poblacional multiplicando la población actual por la tasa de crecimiento anual
# Dividimos entre 100 ya que no se pueden trabajar con porcentajes
crecimientoA = paisA * (6 / 100)
# Dividimos entre 100 ya que no se pueden trabajar con porcentajes
crecimientoB = paisB * (3 / 100)

# Revisamos que el país "A" tenga una población menor a la del país "B" para que el programa cumpla su propósito
if (paisA < paisB):
    # Mientras la población del país "a" sea menor a la del país "b"
    while (paisA < paisB):

        # Incrementar la población de ambos países según la tasa de crecimiento
        paisA = int(paisA + crecimientoA)
        paisB = int(paisB + crecimientoB)

        # Incrementamos la variable "año" ya que el proceso anterior corresponde al crecimiento anual
        año = año + 1

        # Entregamos al usuario la población correspondiente de cada país y el año
        print(f'La población del país A, al año {año}, es de: {paisA}')
        print(f'La población del país B, al año {año}, es de: {paisB}\n')
    # Resultado final
    print(
        f'El país "A" excedió la población del país "B" en {año} años con una población de {paisA} vs {paisB}')
else:
    print('El país "A" debe tener una población menor a la del país "B"')
