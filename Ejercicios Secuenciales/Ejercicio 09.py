#Ejercicio 9: Prestamo bancario
# Un cliente solicita un prestamo que debera pagar en 12 meses con interes fijo mensual de l 2%.
#El usuario ingresa el monto solicitado, y el prorgama debe calcular:
#EL monto total a devolver,
#El valor de cada cuota mensual.

prestamo = float(input("ingrese su prestamo a pagar: "))
cant_interes = float(input("ingrese el interes que se aplica: "))
interes = cant_interes / 100
cuota_interes = prestamo * ((1+interes)**12)
print(f"la cuota con el 2% de interes a pagar es de {cuota_interes/12}")
print(f"El total a pagar es: ${cuota_interes}")

