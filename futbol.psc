Algoritmo futbol //ingreso de datos
	Escribir  "Ingrese la cantidad de partidos ganados del equipo: "
	Leer partidosGanados
	Escribir "Ingrese la cantidad de partidos empatados del equipo: "
	Leer partidosEmpatado
	Escribir  "Ingrese la cantida de partidos perdidos del equipo: "
	Leer partidosPerdidos
	
	// calculos necesarioas para llegar al resultado
	puntosEquipo = (partidosGanados * 3) + (partidosEmpatado * 1) + (partidosPerdidos * 0)
	
	//Resultado
	Escribir "El equipo tiene ",puntosEquipo, " puntos hasta el momento, luego de jugar ",partidosGanados + partidosEmpatado + partidosPerdidos, " partidos"
	
FinAlgoritmo
