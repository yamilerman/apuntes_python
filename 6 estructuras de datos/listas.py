#Listas: colección (array) que permite almacenar múltiples elementos en una sola variable
#Caracteristicas: ordenanda (podemos ingresar a un elemento por índice) y es mutable

 #indices  0            1          2      3
frutas = ["naranja", "manzana", "pera", "pera"] #Permite duplicados

#Para ingresar a un solo elemento de la lista
print(frutas[0])

#Saber la cantidad de elementos que tiene la lista
longitud = len(frutas)
print(longitud)

listaStrings = ["alfa", "beta", "gama"]
listaNumbers = [1,2,3]
listaBooleans = [True, True, False]
listaMixta = ["alfa", 2, True]
print(listaMixta)

#Para saber que tipo de dato es: "list" en este caso
tipo = type(listaBooleans)
print(tipo)

#Construir lista desde constructor
listaDesdeConstructor = list(("Beta", 3, True))
print(listaDesdeConstructor)

#Acceder a los datos
naranja = frutas[0]
parteLista = frutas[1:3] #Desde el 1 hasta el 3 no inclusive
desdeComienzo = frutas[:2]#Desde el comienzo hasta el 2 no incluido
hastaFinal = frutas[2:]#Desde el 2 hasta el final

#verificar si existe un elemento
if "manzana" in frutas: #Utilizando la palabra in podemos saber si un elemento está presente
    print("Sí, está incluido")

#Como cambiar los datos de la lista
#indices        0             1        2             3           4
tecnologias = ["Python", "Django", "JavaScript", "Reactpy" , "Pandas"]

tecnologias[3] = "TensoFlow" #Reemplazar el elmento de in índice particular
tecnologias[2:4] = ["Flask", "NumPy"] #Reemplazar una parte de la lista

#Agregar elementos:
tecnologias.insert(2,"Scrapy") #Insertar un nuevo elemento en un índice especifico
tecnologias.append("TensorFlow") #Agregamos un elemento nuevo al final de la lista

frontend = ["Angular", "React", "Vue"]
tecnologias.extend(frontend) #Agregar cualquier tipo de colección a una lista (fusión)

#Quitar elementos:
tecnologias.remove("Vue") #Se remueve el elemento que coincida con lo que pasemos como argumento
tecnologias.pop() #POdemos eliminar un elemento de un indice especifico y si no especificamos se eliminará el último
del tecnologias[7] #Usando la palabra del podemos especificar el elemento a eliminar

listaABorrar = ["Python", "Django", "JavaScript", "Reactpy" , "Pandas"]
listaABorrar.clear() #Vacia la lista

#Recorrer lista
for tecnologia in tecnologias:
    print(tecnologia)

#acceso al indice i de indice
for i in range(len(tecnologias)):
    print(f"{i+1}. {tecnologias[i]}")

#shorthand para recorrer lista
[print(tecnologia) for tecnologia in tecnologias]

#Ejemplo practico:

listaConY = []

for tecnologia in tecnologias:
    if "y" in tecnologia:
        listaConY.append(tecnologia)
print(listaConY)

#            lo que se agrega | el bucle                  | la condición
lista2ConY = [tecnologia.upper() for tecnologia in tecnologias if "y" in tecnologia] #Shorthand del ejemplo de arriba
print(lista2ConY)

#Ordenar lista
print(tecnologias)
tecnologias.sort()#En caso de no especificar ordenara alfabéticamente o de forma asc
print(tecnologias)

#Oden forma desc
numeros = [3,7,6,9,2,5,8]
numeros.sort(reverse=True)
print(numeros)

tecnologias.reverse()#Ordena exactamente al revés tal cual estaba la lista

#Copiar una lista
meses = ["enero", "febrero", "marzo" , "abril"]
meses2 =["mayo" , "junio" , "julio" , "agosto"]
copiaMeses = meses.copy() #Copia exacta de la lista original
print(copiaMeses)

copiaMeses2 = list(meses) #usando el constructor
print(copiaMeses2)

#Unir dos listas
joinMeses = (meses + meses2) #Podemos juntar la lista (JOIN) utilizando el simbolo +
print(joinMeses)

meses.extend(meses2) #Junta las dos listas en la lista mencionada
print(meses)
