'''
-----------------------------
 RETO N°2
 Estación meteorológica
-----------------------------
 Imagina que desarrollas software para una estación meteorológica automática. El dispositivo registra la temperatura del aire cada hora y lo hace durante todo el mes. Diseñaremos una lista que almacene todos estos resultados.
-----------------------------
'''
temps = [[0.0 for h in range (24)] for d in range (31)]
# La matriz se actualiza mágicamente aquí

# Temperatura promedio al mediodía
suma = 0.0

for day in temps:
  suma += day[11]

promedio = suma / 31
print("Temperatura promedio al mediodía:", promedio)

# Temperatura más alta
mas_alta = -100.0

for day in temps:
  for temp in day:
    if temp > mas_alta:
      mas_alta = temp

print("La temperatura más alta fue:", mas_alta)

# El día más caluroso
hotDays = 0

for day in temps:
  if day[11] > 20.0:
    hotDays += 1

print(hotDays, " fueron los días calurosos.")
