##Operadores lógicos (and, or, not)
edad = 17
tramite = edad >= 18 and edad <= 65 #Devuelve true si cumplimos con las 2 condiciones dadas
semaforo = "Rojo"
cruzar = semaforo == "Verde" or semaforo = "Amarillo" #Devuelve true si cumplimos al menos con 1 de las 2 condiciones dadas
verdad = True
negcaion = not verdad #Niega la estructura siguiente

##Operadores de identidad (is, is not)
nombre = "Siria Lerman"
profesora = "Siria Lerman"
alumno = "Ignacio"
sonElMismo = nombre is profesora #Nos devuelve True si son iguales
sonDistintos = profesora is not alumno #Nos devuelve True si son distintos

##Operadores de pertenencia (in, not in)
palabra = "Mundo"
palabra2 = "Mercurio"
texto = "Hola Mundo"
pertenece = palabra in texto #Nos devuelver True si pertenece
noPertenece = palabra2 not in texto #Nos devuelve True si no está presente