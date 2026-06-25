# Acceso a caracter determinado 
nombre= "Roberto"
print(nombre[0])

print(nombre[-2]) # Accede al ultimo caracter de la cadena

# Slicing → extraer porciones de la cadena 

cadena="buenos dias"
print(cadena[0:8]) 
print(cadena[::2]) # Imprime cada dos caracteres de la cadena


# Metodos utiles en cadenas de texto 
cadena_con_espacios= " Hola Mundo de Nuevo "
cadena_sin_espacios = "Hola mundo sin Espacios"
#Strip - Elimina espacios al inicio y al final de la cadenant(cadena_con_espacios)
print(cadena_con_espacios)
print(cadena_con_espacios.strip())

# Upper - Convierte a mayusculas
print(cadena_sin_espacios.upper())
# Lower - Convierte a minusculas 
print(cadena_sin_espacios.lower())
# replace - Reemplaza una subcadena por otra
print(cadena_sin_espacios.replace("o","0"))
print(cadena_sin_espacios.replace("sin",'---'))
# Split - Divide la cadena en una lista de sub cadenas
print(cadena_sin_espacios.split())

# fstrings - Formateo de cadenas de texto
print("--------------------------------")
edad = 36
print(f"el doble de tu edad es {edad * 2}")

print("--------------------------------")
 # Ingresar datos por teclado input() - Esto siempre regresa un texto 

"""
tu_edad= input("Ingresa tu edad : ")
print(f"la edad insertada es : {tu_edad}")
print(f"El doble de tu edad es: {int(tu_edad) * 3}")
"""
print("--------------------------------")

for i in range(5):
    print(f"El valor de i es: {i}")

print("-------------------")

for l in cadena_sin_espacios.split():
    print(f"Los elementos de la lista son: {l} ")



