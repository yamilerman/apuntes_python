#creando una lista (se pueden modificar y empieza desde el índice 0)
lista = ["Yamila Lerman", "Yami Lerman",True, 1.70] 

#esto es válido
lista[3] = "Sonido"

#creando una tupla (no se puede modoficar, empieza desde el índice 0)
tupla = ("Yamila Lerman", "Yami Lerman",True, 1.70)

#esto no
#tupla[3] = "Sonido"

#range: es una secuencia de números generada dentro de un rango

rango = range(1,10)

#creando un conjunto (set) puedo redifinirlo pero no puedo modificar cada elemento en particular no se puede acceder al indice del conjunto, no permite repetir valores, se puede recorrer con bucle, se puede modificar
conjunto = {"Yamila Lerman", "Yami Lerman",True, 1.70}

#frozenSet ([]): colección desordenada de elementos únicos e inmutables
conjunto_inmutable = frozenset([1,2,2,4])

#creando un diccionario (dict) (ingreso a los valores a través de la clave no tiene índice porque es desordenado y es mutable, puede tener elementos repetidos) (la estructura es key : value y separamos con comas)
diccionario = {
    'nombre' : 'Pergamino',
    'canal' : 15,
    'altura' : True, 
    'dato_duplicado' : 'Pergamino'
}

print(diccionario['nombre'])


