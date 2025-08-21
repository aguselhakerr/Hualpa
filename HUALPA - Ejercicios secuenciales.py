#Ejerciocio 3: Un maestro desea saber que porcentaje de hombres y qué porcentaje de mujeres hay en un grupo

#cant_h = int(input("ingrese la cantidad de hombres"))
#cant_m = int(input("ingrese la cantidad de mujeres"))
#total_alumnos = cant_h + cant_m
#print(f"la cantidad de alumnos es de {total_alumnos}")
#total_h = (cant_h * 100)/total_alumnos
#print(f"total mujeres: {total_m}")
####total_m = (cant_m * 100)/total_alumnos
#print(f"total hombre: {total_h}")


# Un profesor prepara tres cuestionarios para un evaluación final: A, B, C.
#Se sabe que se tarda 5 minutos en revisar el cuestionario A, 
# 8 en revisar el cuestionario B
#6 en el cuestionario C.
# La cantidad de exámenes de cada tipo se entran por teclado
#¿Cuantas hora y cuantos minutos se tardará en revisar todas las evaluaciones?


#A=5; B=8; C=6
#print("Ingrese la cantidad de exmámenes resueltos de cada tipo.")
#cant_examA = int(input("A:")); cant_examB = int(input("B:")); cant_examC = int(input("C:"))
#min = (cant_examA *A)+ (cant_examB*B) + (cant_examC*C) ; horas = min/60 ; segundo = min*60
#print(f"\nVa a tardar {min} minutos en terminar de corregir.",f"\nVa a tardar {horas} horas en terminar de corregir.",f"\nVa a tardar {segundo} segundos en terminar de corregir." )

#Ejercicio 9: Prestamo bancario
# Un cliente solicita un prestamo que debera pagar en 12 meses con interes fijo mensual de l 2%.
#El usuario ingresa el monto solicitado, y el prorgama debe calcular:
#EL monto total a devolver,
#El valor de cada cuota mensual.

#prestamo = float(input("ingrese su prestamo a pagar"))
#cant_interes = input("ingrese el interes que se aplica")
#interes = cant_interes / 100
#cuota_interes = prestamo + (prestamo * interes)
#print(f"la cuota con el 2% de interes a pagar es de {cuota_interes/12}")
#print(f"El total a pagar es {cuota_interes}")
#monto_total = float(input("ingrese su prestamo a pagar: "))
#ms = monto_total / 12
#interes_mensual = float(input("Ingrese el porcentaje mensual: "))
#mt_porcentaje = (ms * (1+(interes_mensual/100))) *12
#print(f"el monto total con el 2% de interes es de {mt_porcentaje}")




#Monto: 1.000 a  12 meses con 2%: 1.010,87


#Cliente:
#Monto_solicitar
#cantidad_meses [12;72]
#es_Veraz (No)
#Ingresos_netos_mensuales if(Ingresos_netos_mensuales 30% < cuota_mensual)



#Ejercicio 6: Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. 
# Dicha calificación se compone de los siguientes porcentajes:
#	55% del promedio de sus tres calificaciones parciales.
#	30% de la calificación del examen final.
#	15% de la calificación de un trabajo final.


#parcial1 = float(input("Ingrese la calificación del primer parcial: "))
#parcial2 = float(input("Ingrese la calificación del segundo parcial: "))
#parcial3 = float(input("Ingrese la calificación del tercer parcial: "))

#parciales = (parcial1 + parcial2 + parcial3) / 3
#promedio_parciales = parciales* 0.55

#examen_final = float(input("Ingrese la calificación del examen final: "))
#promedio_examen = examen_final * 0.30
#trabajo_final = float(input("Ingrese la calificación del trabajo final: "))
#promedio_trabajo = trabajo_final * 0.15

#calificacion_final = (promedio_parciales) + (promedio_examen) + (promedio_trabajo)

#print(f"La calificación final es: {calificacion_final}")



#Ejercicio 7: Conversión de divisas
#Un programa que lea un monto en dólares y lo convierta a pesos colombianos, argentinos y euros usando tasas de cambio fijas 
# definidas en el código.

#cop = 4030.63    
#ars = 1313.02   
#eur = 0.86   

#usd= float(input("Ingrese el monto en dólares (USD): "))

#monto_cop = usd*cop
#monto_ars = usd*ars
#monto_eur = usd*eur

#print(f"{usd} USD equivalen a {monto_cop} pesos colombianos.")
#print(f"{usd} USD equivalen a {monto_ars} pesos argentinos.")
#print(f"{usd} USD equivalen a {monto_eur} euros.")


#Ejercicio 8: Viaje en auto
#Un auto consume 8 litros cada 100 km. El usuario ingresa la distancia en km y el precio de la gasolina por litro.
#El programa debe calcular:
#a) cuántos litros se necesitan,
#b) cuánto costará el viaje,
#c) y cuántas horas tardará si la velocidad promedio es de 90 km/h.

#distancia = float(input("Ingrese la distancia a recorrer en km: "))
#precio_litro = float(input("Ingrese el precio de la gasolina por litro: "))

#litros_necesarios = (distancia * 8) / 100
#costo_viaje = litros_necesarios * precio_litro
#tiempo_horas = distancia / 90

#print(f"Litros necesarios: {litros_necesarios} L")
#print(f"Costo del viaje: ${costo_viaje}")
#print(f"Tiempo estimado de viaje: {tiempo_horas} horas")

#Ejercicio 10: Cliente
# Solicita un préstamo, debe ingresar:
# - Monto a solicitar
# - Cantidad de meses (entre 12 y 72)
# - Si está en Veraz (solo puede continuar si responde 'No')
# - Ingresos netos mensuales (la cuota no debe superar el 30% de este valor)

monto = float(input("Ingrese el monto a solicitar: "))
meses = int(input("Ingrese la cantidad de meses (12 a 72): "))
while meses < 12 or meses > 72:
    meses = int(input("Cantidad inválida. Ingrese la cantidad de meses (12 a 72): "))

es_veraz = input("¿Está en Veraz? (Si/No): ")
if es_veraz == "no" or es_veraz == "No" or es_veraz == "NO" or es_veraz == "nO":
    print("No es posible otorgar el préstamo.")

if es_veraz == "si" or es_veraz == "Si" or es_veraz == "SI" or es_veraz == "sI":
    interes_mensual = 0.02
    cuota = (monto * (1 + interes_mensual * meses)) / meses
    print(f"La cuota mensual es: ${cuota:.2f}")
    ingresos = float(input("Ingrese sus ingresos netos mensuales: "))
    if cuota > ingresos * 0.3:
        print("El préstamo no puede ser otorgado: la cuota supera el 30% de sus ingresos.")
    else:
        total_a_pagar = cuota * meses
        print(f"Préstamo aprobado.")
        print(f"Cuota mensual: ${cuota:.2f}")
        print(f"Total a pagar: ${total_a_pagar:.2f}")

if es_veraz != "si" and es_veraz != "Si" and es_veraz != "SI" and es_veraz != "sI" and es_veraz != "no" and es_veraz != "No" and es_veraz != "NO" and es_veraz != "nO":
    print("Respuesta inválida. Por favor, responda 'Si' o 'No'.")