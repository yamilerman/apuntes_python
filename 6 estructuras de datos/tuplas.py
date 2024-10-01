#Tupla: colección (array) que permite almacenar múltiples elementos en una sola variable
#Caracteristicas: colección ordenada e inmutable de elementos(cada elemento tendrá un índice)

vehiculos = ("bicicleta", "moto", "auto", "caminoneta", "avion", "barco")

longitud = len(vehiculos) #Saber la longitud de la tupla
print(longitud)

tipo = type(vehiculos) #Nos dice que tipo es <class 'tuple'>
print(tipo)

tuplaConstructor = tuple(("Esta es una tupla", 2, True)) #Con el constructor de tupla podemos crear una
print(tuplaConstructor)
print(type(tuplaConstructor))

#Acceso a traves de indice
elemento1 = vehiculos[2]
elemento2 =vehiculos[0]
print(elemento1, elemento2)

rango = vehiculos[3:5]
desdeInicio = vehiculos[:3]
hastaFinal = vehiculos[3:]
print(hastaFinal)

#Como puedo hacer para obtener una tupla con las caracteristicas que yo necesito?[Truco para modificar tupla]

listaVehiculos = list(vehiculos) #en una nueva variable volcar la tupla como lista
listaVehiculos[3] = "camión" #hacer el cambio que queriamos hacer
listaVehiculos.append("crucero")
vehiculos = tuple(listaVehiculos) #asignar a la tupla la lista modificada convertida en tupla
print(vehiculos)

#Desempaquetamiento (aplica para todas las estructuras de datos)
(a,b,c,d,e,f,g) = vehiculos #se asigna cada elemento a una variable correspondiente a la posicion
print(a)

(bici, moto, *cuatroRuedas, avion, barco, crucero) =vehiculos #con el asterisco podemos agrupar parte del desempaquetamiento
print(cuatroRuedas)

#Recorrer tupla con bucle

for vehiculo in vehiculos:
    print(vehiculo)

#acceso al indice i de indice
for i in range(len(vehiculos)):
    print(f"{i+1}. {vehiculos[i]}")

#shorthand para recorrer la tupla
[print(vehiculo) for vehiculo in vehiculos]

#Join de tuplas (unir tuplas)

citricos = ("naranja", "limon", "pomelo")
tropical = ("papaya", "coco")

frutas = citricos + tropical #con el + unimos las dos tuplas en una nueva tupla
print(frutas)
print(type(frutas))

