print("***manejo de listas***")

mi_lista = [1, 2, 3 ,4 , 5]

print(f"{mi_lista} ---> Lista original")
 
#Largo de una lista 
print(f"largo de una lista: {len(mi_lista)}")

# Acceder a los elementos de una lista 

print(f"accedemos al valor  del indice 4 : {mi_lista[4]}")

# Cambiar algun elemento de la lista 
mi_lista[1] = 10
print(f"modificamos el valor del indice 1: {mi_lista[1]}")

#agregamos un elemento a  la lista 
mi_lista.append(6)
print(f"{mi_lista} --> se agregó el elemento 6 ")

# añadir un elemnto de la lista en un indice cualquier
mi_lista.insert(2, 7)
print(f"{mi_lista} --> se añadió el elemento 7 en el indice 2")

# Eliminar elementos de una lista
#Usando el metodo remove 
mi_lista.remove(7)
print(f"{mi_lista} --> Eliminamos el elemento 7 de la lista")
#Removemos  por indice con el metodo pop
mi_lista.pop(0)
print(f"{mi_lista} --> Se eliminó el indice 0 de la lista")
#Eliminar usando la palabra del
del mi_lista[0]
print(f"{mi_lista} --> Se eliminó el indice 0 de la lista")

# Obterner sublistas+
sublista = mi_lista[1:3] #Genera una sublista  del indice 1 al 2(3 no se incluye)
print(f"{sublista} sublista")

