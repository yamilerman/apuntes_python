#Es la estructura que nos permite tomar un flujo u otro según una condición
#La palabra reservada es obligatoria en la estructura condicional pero elif y else son opcionales


ingreso_mensual = 900

if ingreso_mensual > 10000: #Si confirma que la primera condición es real se queda ahí no toma el elif
    print("estás bien en cualquier parte del mundo")
    
elif ingreso_mensual > 1000: #es else if pero se escribe elif
    print("estás bien económicamente en latinoamérica")
    
elif ingreso_mensual > 500: 
    print("estás bien económicamente en argentina")
     
else:
    print("sos pobre") # Si no cumplió ninguna de las condiciones anteriores realiza esta linea de código


#Ejemplo
#Objetivo: entrar a un boliche

edad = 61 

if edad >= 18 and edad <= 60:
    print("Podés entrar")
else: #If anidado
    if edad < 18:
        print("No podes entrar, sos menor de edad")
    else:
        print("Este boliche sólo admite personas hasta 60 años")


#Shorthands (condicionales de una sola linea)

a = 5
b = 2

if a > b: print(f"{a} es mayor que {b}") #Shorthand del if solo

#Ejecución si es verdadero|condición|Ejecución si es falso
print("B es mayor que A") if b > a else print("A es mayor que B") # Shorthand de if + else

