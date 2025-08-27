#Ejerciocio 3: Un maestro desea saber que porcentaje de hombres y qué porcentaje de mujeres hay en un grupo

cant_h = int(input("ingrese la cantidad de hombres: "))
cant_m = int(input("ingrese la cantidad de mujeres: "))
total_alumnos = cant_h + cant_m
print(f"\nLa cantidad de alumnos es de {total_alumnos}")
total_h = (cant_h * 100)/total_alumnos
total_m = (cant_m * 100)/total_alumnos
print(f"total mujeres: {total_m} %")
print(f"total hombre: {total_h} %")