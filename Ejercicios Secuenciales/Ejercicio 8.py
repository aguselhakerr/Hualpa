#Ejercicio 8: Viaje en auto
#Un auto consume 8 litros cada 100 km. El usuario ingresa la distancia en km y el precio de la gasolina por litro.
#El programa debe calcular:
#a) cuántos litros se necesitan,
#b) cuánto costará el viaje,
#c) y cuántas horas tardará si la velocidad promedio es de 90 km/h.

distancia = float(input("Ingrese la distancia a recorrer en km: "))
precio_litro = float(input("Ingrese el precio de la gasolina por litro: "))

litros_necesarios = (distancia * 8) / 100
costo_viaje = litros_necesarios * precio_litro
tiempo_horas = distancia / 90

print(f"Litros necesarios: {litros_necesarios} L")
print(f"Costo del viaje: ${costo_viaje}")
print(f"Tiempo estimado de viaje: {tiempo_horas} horas")