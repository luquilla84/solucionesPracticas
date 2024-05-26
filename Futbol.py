#Datos de entrada
partidos_ganados = int(input("Ingrese la cantidad de partidos ganados del equipo: "))
partidos_empatados = int(input("Ingrese la cantidad de partidos empatados del equipo: "))
partidos_perdidos = int(input("Ingrese la cantidad de partidos perdidos del equipo: "))

#calculos necesarios para llegar al resultado
total_puntos = 0

if partidos_ganados > 0:
    total_puntos += partidos_ganados * 3

if partidos_empatados > 0:
    total_puntos += partidos_empatados * 1

if partidos_perdidos > 0:
    total_puntos += partidos_perdidos * 0

total_partidos_jugados = partidos_ganados + partidos_empatados + partidos_perdidos

#Resultado
print(f"El equipo tiene {total_puntos} puntos hasta el momento.")
print(f"Luego de jugar {total_partidos_jugados} partidos.")