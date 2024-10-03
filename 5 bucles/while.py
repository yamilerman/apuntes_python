#Bucles: es una estructura que se repite mientras la condición sea verdadera

x = 1

while x <= 10:
    print(f"Hola a todos estoy dentro de un bucle y x vale {x}")
    x += 1 #(para cortar el bucle control c por si no le puse acción para que la condición sea false)

    if x == 5:
        break #Esto hace que salga del bucle

    if x == 15:
        continue #Saltea las lineas de acá en adelante

else:
    print(f"Ya no se cumplió la condición del bucle porque x es {x}")


#Ejemplo

while True: 
    print("No te olvides de guardar el archivo")
    respuesta = input("¿Desea salir? (s/n)").strip().lower()
    if respuesta == 's':
        break


#Control de bucles
#Break: en este ejemplo, el bucle while se ejecuta indefinidamente debido a la condición True. Sin embargo, dentro del bucle se utiliza una estructura condicional if para verificar si contador es igual a 5. Cuando se cumple esta condición, se ejecuta la instrucción break, lo que hace que el bucle se detenga y el flujo de ejecución continúe con la siguiente instrucción fuera del bucle.
contador = 0
while True:
    print(contador)
    contador += 1
    if contador == 5:
        break

#Continue: en este ejemplo, el bucle for itera sobre los números del 0 al 9 utilizando la función range(). Dentro del bucle, se verifica si el número es divisible por 2 utilizando el operador de módulo %. Si el número es divisible por 2 (es decir, si es par), se ejecuta la instrucción continue, lo que hace que se salte el resto del bloque de código y se pase a la siguiente iteración del bucle. Como resultado, solo se imprimirán los números impares.
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
#Pass: en este ejemplo, el bucle for itera sobre los números del 0 al 4, pero no se realiza ninguna acción dentro del bucle debido a la instrucción pass. Esto puede ser útil cuando se está desarrollando un programa y se desea reservar un bloque de código para implementarlo más adelante.
for i in range(5):
    pass
