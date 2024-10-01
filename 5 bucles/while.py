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
    