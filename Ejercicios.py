"""
ejercicio 1
usar el condicional simple para saber si una persona es mayor de edad

"""
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Sos mayor de edad.")



"""
ejercicio 2
usar el condicional completo para saber si hace calor o frio segun
la temperatura ingresada.

"""
temperatura = int(input("Ingrese la temperatura actual: "))
if temperatura >= 25:
    print("es un dia de calor")
else:
    print("es un dia frio")

"""
ejercicio 3
usar el condicional parcial con expresion logica compuesta AND para saber
si una persona puede conducir

"""
edad = int(input("Ingrese su edad: "))

if edad >= 18 and edad < 85:
    print("Puede manejar")

"""
Ejercicio 4
usar el condicional completo con expresion logica compuesta OR para
si una persona tiene que ir a dormir o no.

"""
hora = int(input("Ingrese hora actual: "))
if hora >=22 or hora < 6:
    print("Debes ir a dormir.")
else:
    print("Puedes seguir jugando.")