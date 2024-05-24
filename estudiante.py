nota1 = float(input("introduce la nota de la materia 1: "))
nota2 = float(input("introduce la nota de la materia 2: "))
nota3 = float(input("introduce la nota de la materia 3: "))
nota4 = float(input("introduce la nota de la materia 4: "))
nota5 = float(input("introduce la nota de la materia 5: "))

sumaTotal = 0
contador = 0

if nota1 >= 0:
    sumaTotal += nota1
    contador += 1

if nota2 >= 0:
    sumaTotal += nota2
    contador += 1

if nota3 >= 0:
    sumaTotal += nota3
    contador += 1

if nota4 >= 0:
    sumaTotal += nota4
    contador += 1   

if nota5 >= 0:
    sumaTotal += nota5
    contador += 1

if contador > 0:
    promedio = sumaTotal / contador
    print(f"la suma de las notas es: {sumaTotal}, y el promedio de las notas es: {promedio} ")



