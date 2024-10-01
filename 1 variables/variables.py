#Pueden empezar con una letra o guión bajo
#No pueden iniciar con un número
#Sólo pueden contener caracteres alfanuméricos y guiones bajos (A-z 0-9 _)
#No se pueden usar palabras reservadas de Python para definirlas (keywords)

#Convenciones de escritura de variables
#Definiendo una variable con snake_case , es la recomendación de Python 
nombre_de_tu_tio = "Matias Pampo" 

#Definiendo una variable con camelCase
nombreCompleto = "Lucas Araujo"

#Definiendo una variable con PascalCase
NombreCompletoAlumno = "Ignacio Mirsi"

#Concatenar con +
bienvenida = "Hola " + nombre_de_tu_tio + " ¿Cómo estas?"
print (bienvenida)

#Concatenar con f-string
bienvenida = f"Hola {nombre_de_tu_tio} ¿Cómo estas?"
print (bienvenida)

resultado = f"El resultado de 69 x 63 es {60 * 63}"
print(resultado)

# del bienvenida : operador para borra datos

#Operador de pertenencia (in y not in)
#para buscar (ojo con minúsculas y mayúsculas ya que Python es caseSensitive, interpreta como distinto una mayúscula de una minúscula)

print ("Lucas" in bienvenida) #true
print ("Lucas" not in bienvenida) #false

#Multiasignación
x, y, z =5, 7, 9 #print x=5 y=7 z=9
a = b = c = "Siria Lerman" #print a = Siria Lerman b = Siria Lerman c = Siria Lerman

#Desde colecciones
frutas = ["naranjas", "bananas", "manzanas"]
m, n, b = frutas #print m = naranjas n = bananas b = manzanas

#Uso de print y salidas
txt = "Hola "
txt2 = "desde "
txt3 = "Argentina"

print(txt + txt2 + txt3) #print Hola desde Argentina con la , (coma) podemos concatenar datos de distinto tipo

# Variables globales vs Variables de Scope

variableGlobal = "Esta variable está para todo el programa"

def funcion():
    variableScope = "Esta variable está disponible dentro de la función"
    print(variableGlobal)
    print(variableScope)
funcion()

print(variableGlobal) #se imprime correctamente
# print(variableScope) da error al imprimirse fuera de la función 
