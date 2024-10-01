#Funciona lambdas: funciones anónimas sin nombre y cortas es decir de una sola linea de código

#SINTAXSIS:
# lambda  arg1, arg2, arg3 : retorno

def suma(a,b):
    return a + b

sumar_lambda = lambda a,b : a + b
print(sumar_lambda(5,5))

#Ejemplo:

def creador_funciones_multipicacion(n):
    return lambda a : a * n

cuadriplicador = creador_funciones_multipicacion(4)
triplicador = creador_funciones_multipicacion(3)
duplicador = creador_funciones_multipicacion(2)

print(duplicador(5))
print(triplicador(5))
print(cuadriplicador(5))

#Ejemplo práctico de lambda en filter

numeros = [1,2,3,4,5,6,7,8,9,10]
pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)


