'''
-----------------------------
 EJERCICIO N°1
 Algoritmo del ordenamiento burbuja
-----------------------------
'''

miLista = [8, 10, 6, 2, 4] # Lista para ordenar
intercambio = True # Al inicio debe ser True para ingresar al bucle

while intercambio:
  intercambio = False # no hay intercambios hasta ahora
  for i in range(len(miLista) - 1):
    if miLista[i] > miLista[i + 1]:
      intercambio = True # ¡Ocurrió un intercambio!
      miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print(miLista)
