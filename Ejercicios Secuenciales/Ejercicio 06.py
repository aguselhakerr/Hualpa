#Ejercicio 6: Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. 
# Dicha calificación se compone de los siguientes porcentajes:
#	55% del promedio de sus tres calificaciones parciales.
#	30% de la calificación del examen final.
#	15% de la calificación de un trabajo final.

parcial1 = float(input("Ingrese la calificación del primer parcial: "))
parcial2 = float(input("Ingrese la calificación del segundo parcial: "))
parcial3 = float(input("Ingrese la calificación del tercer parcial: "))

parciales = (parcial1 + parcial2 + parcial3) / 3
promedio_parciales = parciales* 0.55

examen_final = float(input("Ingrese la calificación del examen final: "))
promedio_examen = examen_final * 0.30

trabajo_final = float(input("Ingrese la calificación del trabajo final: "))
promedio_trabajo = trabajo_final * 0.15

calificacion_final = (promedio_parciales) + (promedio_examen) + (promedio_trabajo)

print(f"La calificación final es: {calificacion_final}")
