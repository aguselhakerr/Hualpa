#Ejercicio 10: Cliente
# Solicita un préstamo, debe ingresar:
# - Monto a solicitar
# - Cantidad de meses (entre 12 y 72)
# - Si está en Veraz (solo puede continuar si responde 'No')
# - Ingresos netos mensuales (la cuota no debe superar el 30% de este valor)
#Cliente:
#Monto_solicitar
#cantidad_meses [12;72]
#es_Veraz (No)
#Ingresos_netos_mensuales if(Ingresos_netos_mensuales 30% < cuota_mensual)


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