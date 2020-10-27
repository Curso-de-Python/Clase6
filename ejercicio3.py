'''
-----------------------------
 EJERCICIO N°3
 Práctica con listas
-----------------------------
 Encontraremos la ubicación de un elemento dado dentro de una lista
-----------------------------
'''

miLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Encontrar = 5
Encontrado = False

for i in range(len(miLista)):
  Encontrado = miLista[i] == Encontrar
  if Encontrado:
    break

if Encontrado:
  print("Elemento encontrado en el índice", i)
else:
  print("ausente")
  
