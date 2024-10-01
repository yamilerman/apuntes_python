        #012345....        
texto = "Estoy estudiando y profundizando python con sergie code y dalto"

#str (string): Texto o cadena de caracteres
comillas_simples = 'Hola'
comillas_dobles = "Hola"
comillas_triples = """Hola"""
comillas_triples_simples = '''Hola''' 

#type
print(comillas_simples)
print(type(comillas_simples))


#Arrays de caracteres
caracter = texto[2] #podemos seleccionar caracter por índice
print(caracter)

#Len (length) (saber el largo del texto)
amplitud = len(texto)
print(amplitud)

# In: para saber si está incluido algo en el texto, recordar que es caseSensitive
print("python" in texto) # devuelve true o false

#Not in: con la palabra reservada not podemos negar y pedir un resultado negativo
print("JavaScript" not in texto)# devuelve true o false

#Slice (cortar) una parte del texto
print(texto[6:16]) #corta incluyendo desde el 6 hasta el 15 porque no incluye el 16 (incluye los start no los stop)
print(texto[:5]) # se imprime el fragmento que vaya desde el comienxo al índice 5 y no lo incluye
print(texto[58:]) # se imprime el fragmento que vaya desde el índice 58 hasta el final
print(texto[-5:])# se imprime el fragmento que vaya desde 5 indices antes del final hasta el final
print(texto[:-57])# se imprime el fragmento desde el comienzo hasta el final 57 caracteres antes del final

#Modificadores de texto (mayúsculas, minúsculas, etc)

texto_nuevo = "Sigo estudiando con mucho compromiso"

mayusculas = texto_nuevo.upper()#obtengo el texto en mayusculas
print(mayusculas)

minusculas = texto_nuevo.lower()#obtengo el texto en minusculas
print(minusculas)

texto_con_espacios = "           hola mundo                 "
sin_espacios = texto_con_espacios.strip() #eliminrá los espacios del comienzo y final
print(sin_espacios)

reemplazo = texto_con_espacios.replace("mundo", "universo")
print(reemplazo)

texto_con_comas = "No, te, olvides, de tomar, agua"
separar_por_comas = texto_con_comas.split(",") #separará e texto por comas y devolverá una lista
print(separar_por_comas)

#Métodos más usados

texto_a_modificar = "este es UN texto A MODIFICAR"
capitalizado = texto_a_modificar.capitalize() # sólo queda la primer letra con mayúscula
print(capitalizado)

esta_comenzando = texto_a_modificar.startswith("este") #devuelve un true - recordar que es CaseSensitive si pongo mayúscula va a decir en este caso que es false
print(esta_comenzando)

esta_finalizando = texto_a_modificar.endswith("MODIFICAR")
print(esta_finalizando)

titulo = texto_a_modificar.title()
print(titulo) #pone en mayúscula cada primera letra de cada palabra

contador = texto_a_modificar.count("e")
print(contador) # cuantas veces aparece la e en minúscula en el texto

encontrador = texto_a_modificar.find("texto")
print(encontrador)# devuelve que la palabra texto comienza en el índice 11


#Concatenar
a= "Hola"
b= " mundo"
c = a + b

print(c)

#fstrings en pagina variables.py f"texto{}"

# Escapes \ (backslash - barra invertida)
escape = "Mi país fav es \"Argentina\""
print(escape)
salto_de_linea = "Quiero hacer un \nsalto de linea"
print(salto_de_linea)
