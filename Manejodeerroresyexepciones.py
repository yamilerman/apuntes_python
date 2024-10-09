#Errores de sintaxis
#Ocurre cuando el código no sigue las reglas de sintaxis de Python, como olvidar dos puntos después de una declaración de función o un bucle
def mi_funcion() # Falta los dos puntos
    print("Hola")

#Error de nombre
#Ocurre cuando se hace referencia a una variable o función que no ha sido definida.
print(variable_no_definida)

#Error de tipo
#Ocurre cuando se realiza una operación con tipos de datos incompatibles, como intentar sumar un número y una cadena.
resultado = 5 + "10"

#Error de índice
#Ocurre cuando se intenta acceder a un índice fuera del rango válido de una lista o secuencia.
lista = [1, 2, 3]
print(lista[3])  # El índice 3 está fuera del rango
