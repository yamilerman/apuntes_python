#Operador de asignacion

x = 10 # = es el operador de asignación más básico
x += 3 # El += le suma el valor al valor anterior
x -= 3 # El -= le resta el valor al valor anterior
x *= 3 # El *= le multiplica el valor al valor anterior
x /= 3 # El /= le divide el valor al valor anterior
x //= 3  
x %= 3  
x **= 3 

#Operadores de comparación (devuelven booleanos, True o False)
igual_que = 5 == 6

distinto_de = 5 != 6

mayor_que = 5 > 6

menor_que = 5 < 6

mayor_o_igual = 5 >= 6

menor_o_igual = 5 <= 6




#calculos combinados

a = 5
b = 10
c = 20

comparacion = a + b < c

print(comparacion)

#comparar usuarios
contraseña_almacenada = "Yami"
contraseña_escrita = "Yami"

print(contraseña_almacenada == contraseña_escrita)

#Nos ayuda a tomar decisiones
#Estructura que devuelven verdadero (las que tiene contenido)
string = bool("Hola")
num = bool(2022)
lista = bool(["pera", "banana", "manzana"])
dict = bool({"nombre": "Yamila Lerman"})

#Estructura que devuelven falso (las que NO tiene contenido)
string2 = bool ("")
num2 = bool(0)
lista2 = bool([])
dict2 = bool({})
none = bool(None)


