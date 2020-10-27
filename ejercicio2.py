'''
-----------------------------
 EJERCICIO N°2
 Algoritmo interactivo del ordenamiento burbuja
-----------------------------
'''
miLista = []
intercambio = True
num = int(input("¿Cuántos elementos deseas ordenar?: "))

for i in range(num):
  val = float(input("Introduce un elemento de la lista:"))
  miLista.append(val) # Inserta el número al final de la lista

while intercambio:    # Algoritmo burbuja
  intercambio = False
  for i in range(len(miLista) - 1):
    if miLista[i] > miLista[i + 1]:
      intercambio = True
      miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print("\nOrdenado:")
print(miLista)
