#Ejercicio 7: Conversión de divisas
#Un programa que lea un monto en dólares y lo convierta a pesos colombianos, argentinos y euros usando tasas de cambio fijas 
# definidas en el código.

cop = 4030.63    
ars = 1313.02   
eur = 0.86   

usd= float(input("Ingrese el monto en dólares (USD): "))

monto_cop = usd*cop
monto_ars = usd*ars
monto_eur = usd*eur

print(f"{usd} USD equivalen a {monto_cop} pesos colombianos.")
print(f"{usd} USD equivalen a {monto_ars} pesos argentinos.")
print(f"{usd} USD equivalen a {monto_eur} euros.")
