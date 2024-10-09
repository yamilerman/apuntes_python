#Errores
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

#Excepciones
#El manejo de excepciones nos permite capturar y manejar errores de manera controlada utilizando las declaraciones try, except y opcionalmente finally.

#Try: El bloque try contiene el código que puede generar una excepción. Si ocurre una excepción dentro del bloque try, el flujo de ejecución se transfiere al bloque except correspondiente.
try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")

#Except: El bloque except especifica el tipo de excepción que se desea capturar y manejar. Puedes tener múltiples bloques except para manejar diferentes tipos de excepciones.
try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")
except ValueError:
    print("Error: Valor inválido")

#Finally: El bloque finally es opcional y se ejecuta siempre, independientemente de si ocurrió una excepción o no. Se utiliza comúnmente para realizar tareas de limpieza o liberación de recursos.
try:
    # Código que puede generar una excepción
    archivo = open("archivo.txt", "r")
    # Realizar operaciones con el archivo
except FileNotFoundError:
    print("Error: Archivo no encontrado")
finally:
    archivo.close()  # Cerrar el archivo siempre, incluso si ocurre una excepción

#Excepciones personalizadas
def funcion():
    # Código que puede generar una excepción personalizada
    if condicion:
        raise Exception("Descripción del error")
try:
    funcion()
except Exception as e:
    print(f"Error: {str(e)}")
#En este ejemplo, se define una función llamada funcion(). Dentro de la función, se verifica una condición y, si se cumple, se genera una excepción utilizando la declaración raise. En lugar de crear una clase personalizada, se utiliza directamente la clase base Exception para generar la excepción.


