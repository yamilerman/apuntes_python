#Diccionario: colección (array) que permite almacenar multiples elementos en una sola variable
#Caracteristicas: Colección de pares clave-valor(key-value) desordenada y mutable

diccionario = {
    "nombre" : "Yami Lerman",
    "youtube": "www.youtube.com/@yamlerman",
    "tecnologias": "['Python', 'JavaScript']",
    "edad" : 35,
    "direccion": {
        "calle" : "Av. Argentina",
        "numero" : 1234, 
        "ciudad" : "Buenos Aires"
    },
    }

tipoDic = type(diccionario) #nos indica el tipo de dato <class 'dict'>
print(tipoDic)

longitud = len(diccionario) #nos indica la cantidad de claves valor que tiene el diccionario
print(longitud)

constructorDiccionario = dict(nombre = "Siria Lerman", youtube = "www.youtube.com/@chichita") #Se puede crear con el constructor
print(constructorDiccionario)

#¿Cómo accedo a cada propiedad? A través de la key
nombre = diccionario["nombre" ]
youtube = diccionario["youtube" ]
tecnologias = diccionario["tecnologias" ]
edad = diccionario["edad" ]
direccion = diccionario["direccion"]

print(nombre)

youtube2 = diccionario.get("youtube")
print(youtube2)

keys = diccionario.keys()
print(keys) #el tipo de datos que devuelve se llama <'dict_keys'>
values = diccionario.values()
print(values) #el tipo de datos que devuelve se llama <'dict_values'>

items = diccionario.items() #nos devuelve tuplas de clave-valor en una lista
print(items)
print(type(items))#el tipo de datos que devuelve se llama <'dict_items'>

if "tecnologias" in diccionario: #comprobamos si una key existe pero no un valor
    print("Sí, existe esta key")

#Cambio de valores en un diccionario

diccionario["tecnologias"] = ["Python", "JavaScript", "NodeJs.", "SQL"]
diccionario.update({"direccion": {
        "calle" : "Av. Siempre viva",
        "numero" : 1234, 
        "ciudad" : "Buenos Aires"}, })
print(diccionario)

#Agregar items
diccionario["profesion"] = "Programadora"
diccionario.update({'comida favorita' : 'Milanesas'})
print(diccionario)

#Eliminar items

diccionario.pop("comida favorita") #elimina un elemento puntual
print(diccionario)
diccionario.popitem()#elimina última característica agregada
print(diccionario)
del diccionario["edad"]
print(diccionario)
diccionario.clear()#esto deja el diccionario vacio

#Bucles (loops) para diccionarios:
curso_python = {
    "nombre" : "Python desde Cero", 
    "duracion" : 8, 
    "dificultad" : "media"
}

for key in curso_python: #el bucle for común hará un recorrido de las keys
    print(f"{key.capitalize()}: {curso_python[key]}")

for value in curso_python.values(): #este bucle recorrerá solo los valores
    print(value)

for key,value in curso_python.items(): #desempaqueto la tupla de cada uno de los elementos de la lista que devuelve items
    print(key,value)

#Copias de diccionarios

copia = curso_python.copy()#copia exacta apuntando a otra dirección de memoria
copia2 = dict(curso_python) #copia usando constructor
print(copia2)


#Acceder a anidados:

empleado1 = {
    "nombre" : "Matias", 
    "edad" : 33
}

empleado2 = {
    "nombre" : "Ana", 
    "edad" : 43
}

empleado3 = {
    "nombre" : "Ignacio", 
    "edad" : 30
}

empresa = {
    "empleado1" : empleado1,
    "empleado2" : empleado2,
    "empleado3" : empleado3,
}

nombreEmpleado1 = empresa["empleado1"]["nombre"]
print(nombreEmpleado1)

for x, obj in empresa.items():
    print(x)
    for y in obj:
        print(f"{y.capitalize()}: {obj[y]}")
        