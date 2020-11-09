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

for dia in temps:
  suma += dia[11]

promedio = suma / 31
print("Temperatura promedio al mediodía:", promedio)

# Temperatura más alta
mas_alta = -100.0

for dia in temps:
  for temp in dia:
    if temp > mas_alta:
      mas_alta = temp

print("La temperatura más alta fue:", mas_alta)

# El día más caluroso
diasCalurosos = 0

for dia in temps:
  if dia[11] > 20.0:
    diasCalurosos += 1

print(diasCalurosos, " fueron los días calurosos.")
