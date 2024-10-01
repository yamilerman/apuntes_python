#Función es un bloque de código autónomo que se ejecuta cuando lo llamamos
#Nos va a servir para atomizar y reutilizar código optimizando el mismo

#Parámetros son la lista de variables dentro de los paréntesis
#Argumentos son los valores que le enviamos a la función cuando es llamada

                #parámetros = variables
def funcion(profesor, curso, femenino):
    profesion = "el profesor"
    if femenino:
        profesion = "la profesora"
    print(f"El curso de {curso} lo dará {profesion} {profesor}")

            #argumentos = valores
funcion("Sergie Code", "Python desde cero", False) #llamo a la función
funcion("Pedro Orozco", "Cocina", False)
funcion("Mariana Mia", "Manejo", True)
funcion("Mercedes Moreau", "Programación inicial", True)

#Variables por defecto / Esto nos dará la posibilidad de NO enviar ese argumento (opcional)
def decir_pais(pais = "Argentina"):
    print(f"El nombre de mi país es {pais}")

decir_pais("Francia")
decir_pais()

#Retornar valores

def suma(a,b):
    return a + b
def resta(a,b):
    return a - b
def multiplicacion(a,b):
    return a * b
def division(a,b):
    return a // b

resultado_suma = suma(2,2)
resultado_resta = resta(2,2)
resultado_multiplicacion = multiplicacion(2,2)
resultado_division = division(2,2)

print(resultado_suma)
print(resultado_resta)
print(resultado_multiplicacion)
print(resultado_division)

#Argumentos arbitrarios (mandar múltiples argumentos según dependa)
#Cuidado porque si el indice del argumento no existe da error la aplicación

def llamar_alumnos(*alumnos):
    print(f"Mi mejor alumna es {alumnos[0]}")
    print(f"Mi alumno mas divertido es {alumnos[3]}")

llamar_alumnos("Daphne", "Benjamin", "Helena", "Bautista")

#Argumentos clave / Key arguments

def cursos(curso1, curso2, curso3):
    print(f"El primer curso que daremos en la academia será {curso1}")
    print(f"el siguiente será el curso de {curso2}")
    print(f"y para finalizar daré el curso de {curso3}")

cursos(curso3= "Matemática", curso1= "Finanzas", curso2= "Inversiones") #Indicaremos a que parámetro corresponde cada argumento

#Argumentos claves arbitarios

def llamar_empleado(**empleado):
    print(f"El aplellido del empleado es {empleado["apellido"]}, y su nombre es {empleado ["nombre"]}")

llamar_empleado(apellido = "Miranda", nombre = "Mila", edad = 35)

#Otros tipos de datos que podriamos pasar:

lista = ["Python", "Flask" , True, 45]
number = 33

def usar_tipos_de_datos(lista, number): #si bien se llaman igual los parámetros estos son internos de la función, si yo llamo a usar_tipos_de_datos y le paso otra lista y otro number me tomará esos
    print(lista)
    print(number)

usar_tipos_de_datos(['Jamaica', 'Francia'], 3)
usar_tipos_de_datos(lista, number)#Ahora le pase como argumentos la lista y el number que habia declarado antes

#Recursion (Recursividad) en una función (llamar a una función dentro de una función, se puede considera en cierta forma un bucle)

#Ejemplo del factorial
#0! = 1
#n! = n * (n-1) para n > 0

def factorial(n):
    #caso base 0! = 1
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

numero = 3
print(f"El factorial de {numero} es {factorial(numero)}")





