
#int (interger): Número entero

numero_entero = 19077753345

#float: Número decimal

numero_decimal = 3.14

#complex: número complejo (parte entera y otra parte imaginaria)

numero_complex = 5 + 2j

print(numero_entero)
print(type(numero_entero))

print(numero_decimal)
print(type(numero_decimal))

print(numero_complex)
print(type(numero_complex))

#Casteo

decimal_desde_entero = float(numero_entero)
entero_desde_decimal = int(numero_decimal)
complejo_desde_entero = complex(numero_entero)
complejo_desde_decimal = complex(numero_decimal)

#Random

import random

aleatorio = random.randrange (1,10) # en número de stop no es incluyente
aleatorio_par = random.randrange(2,11,2) #toma cada 2 desde el 2 al 11 y el 11 no está incluido
aleatorio_impar = random.randrange(1,10,2)#arranca desde el 1 cada 2 números hasta el 9 porque el 10 no está incluido

