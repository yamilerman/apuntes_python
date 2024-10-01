#Sets: colección (array) que permite almacenar múltiples elementos en una sola variable
#Caracteristicas: coleccion desordenada de elementos únicos (no ordenados)
#*Se pueden agregar y eliminar elementos pero los elementos no son "cambiables" ya que no tienen un orden y no puedo acceder a través de ellos por un índice

conjunto= {1, 1, 2, 3, "Llegas con los tiempos", True} # los elementos que estén duplicados serán omitidos

longitud = len(conjunto) # la longitud o cantidad de elementos del conjunto no tomará en cuenta los duplicados
print(longitud)
tipo= type(conjunto) #para saber el tipo <class 'set'>
print(tipo)
conjuntoConstructor = set (("Este", "es" , "un", "conjunto"))#creamos el conjunto usando el constructor Lo crea desordenado

if "conjunto" in conjuntoConstructor:#podemos usar IN para saber si un elemento está presente
    print("Sí está la palabra")

if "Python" not in conjuntoConstructor:#NOT IN para saber si un elemento no está presente
    print("Python no se encuentra en el conjunto")

#Agregar elementos a un conjunto (set)
telefonos = {'Xiaomi','Samsung','Motorola'}
print(telefonos)

telefonos.add('Iphone')#Agregar un elemento
print(telefonos)

telefonos2 = {'Huawei', 'OnePlus', 'Nokia'}
telefonos.update(telefonos2)#Sumamos otra colección(puede ser cualquier colección) a nuestro conjunto
print(telefonos)

#Eliminar elementos (al no tener orden especifico hay que tener mucha precacución con el borrado)
autos = {'Ford', 'Peugeot', 'Ferrari', 'Renault'}
autos.remove('Ferrari')#Se borra un elemento que coincida exactamente con lo pasado por argumento, recordar que Python es caseSensitive (Da un error si el elemento no existe)
autos.discard('Fiat')#Se borra un elemento que coincida exactamente con lo pasado por argumento, recordar que Python es caseSensitive (No da un error si el elemento no existe)

autos.pop() #eliminara de forma aleatoria 
autos.clear()#borra todos los elementos presentes en el conjunto

print(autos)


#Recorrer los elementos con bucles
tecnologias = {'Python', 'C#', 'Java', 'Node'}

for tecnologia in tecnologias:
    print(tecnologia)

#shorthand para recorrer el conjunto se imprimen de forma desordenada
[print(tecnologia) for tecnologia in tecnologias]


#Join de conjunto (Teoria de conjunto de la matematica)

a = {1,2,3,4,5}
b = {1,3,5,7,9}

booleanos = {True, False}

#Union: devuelve todos los elementos de ambos conjuntos. Unir los dos conjuntos (a diferencia del update no modifica el conjunto original)
u = a.union(b) #acepta varios colecciones b, x, y... pueden ser listas o tuplas también
print(u)
u2 = a | b #es exactamente lo mismo que usar union - se lee a o(|) b
print(u2)

# a.update(b) update modifica el conjunto original

#Intersección: va a devolver los elementos que tengan en común ambos conjuntos
i = a.intersection(b)
i2 = a & b # esto es exactamente lo mismo que usar intersection

print(i)

#a.intersection_update(b) intersection_update modifica el conjunto original 

#Comportamiento con booleanos

booleanos_union = a.union(booleanos) #True y 1 se consideran el mismo valor por lo cual solo se agregará False
print(booleanos_union)
booleanos_intersection = a.intersection(booleanos)#La única intersección es True ya que se considera igual a 1
print(booleanos_intersection)

#Diferencias: devolver los elementos del primer conjunto que no estén en el segundo conjunto

d = a.difference(b)
d2 = a - b #es exactamente lo mismo que usar difference

# a.difference_update(b) #Difference_update modifica el conjunto original

print(d)

#Diferencia simetrica: devuelve los elementos que no estén presentes en ambos conjuntos
ds1 = a.symmetric_difference(b)
ds2 = a ^ b # exactamente lo mismo que usar symmetric_difference
print(ds2)
# a.symmetric_difference_update(b) #.symmetric_difference_update modifica el conjunto original



