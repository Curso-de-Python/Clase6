'''
-----------------------------
 EJERCICIO N°5
 Arreglos tridimensionales
-----------------------------
'''
habitaciones = [[[False for h in range(20)] for p in range(15)] for e in range(3)] 

habitaciones[1][9][13] = True 

vacante = 0

for numeroHabitacion in range(20):
  if not habitaciones[2][14][numeroHabitacion]:
    vacante += 1

print("Hay", vacante, "habitaciones disponibles")
