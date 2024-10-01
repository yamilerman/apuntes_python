#Bucles: es una estructura que se repite mientras la condición sea verdadera

tecnologias = ["Python", "JavaScript", "Java", "C#", "Angular", "React", "NodeJS", "Ruby", "R", "Django"]
x = 1

#Cómo iterar una estructura de datos: lista, tupla, etc.
for tecnologia in tecnologias:
    print(f"{x}. {tecnologia}")
    x +=1
else: 
    print("Esas fueron todas las tecnologías que sabe Miriam")

#Cómo iterar un string:
for letra in "Python":
    print(letra)

#Cómo iterar un rango de números:
for x in range(5): #Range imprime desde 0 al número que colocamos sin incluirlo
    print(x)

for x in range (2,7): #Range imprime desde el primer número al segundo sin incluirlo
    print(x)

for x in range (2,11,2): #El tercer parámetro nos sirve para poner intervalos
    print(x)

#Iterar un bucle dentro de otro, anidado

letras = ["a","b", "c"]
numeros = [1,2,3]

for l in letras:
    for n in numeros:
        print(l,n)
        