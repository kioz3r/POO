
# Nuestro primer  hola mundo 
print ("Hola mundo grupo!!")

# Declaracion de tipo de variables
nombre = "roberto"
edad = 36
tienesuenio = True

#Imprimiendo tipo de variables 
print (" la variable nombre es tipo " + str(type(nombre)))
print (" la variable edad es tipo " + str(type(edad)))
print (" la variable tienesuenio es tipo " + str(type(tienesuenio)))

# Conversion de tipos

# Convirtiendo de texto a numero
var_texto = "42"
print (" la variable var_texto es tipo " + str(type(var_texto)))
var_anumero = int(var_texto)
print (" la variable var_anumero es tipo " + str(type(var_anumero)))

#Convercion de numero a texto
var_numero = 3.14  
print ('El tipo de la variable var_numero es: ' + str(type(var_numero)))
var_texto2 = str(var_numero)
print ('El tipo de la variable var_texto2 es: ' + str(type(var_texto2)))


# Ejemplo práctico: calcular promedio de calificaciones
c1, c2, c3 = 8.5, 9.0, 7.5 # asignación múltiple de calificaciones

# verificar los valores de las variables
print(f'Calificación 1: {c1}')
print(f'Calificación 2: {c2}')
print(f'Calificación 3: {c3}')

promedio = (c1 + c2 + c3) / 3  # suma y divide entre 3
print(f'Promedio: {promedio:.2f}')  # muestra 2 decimales → 8.33


# Operadores lógicos  AND
edad = 16
tiene_credencial = True
puede_votar= (edad >= 18) and tiene_credencial
print('¿Puede votar ?: '+ str((puede_votar)))

# Operador Or

es_feriado = False
es_fin_de_semana = False
puedes_descansar = es_feriado or es_fin_de_semana
print("¿Podemos descansar? " + str(puedes_descansar))


# Operador Not 
esta_lloviendo = False
sale_a_pasear = not esta_lloviendo
print("¿Puede salir a pasear ?" + str(sale_a_pasear))


# Cadenas de texto  - Funcion len() para obtener longitud de una cadena
cadena = "dos "
longitud = len(cadena)
print("Total de letras en la cadena es ---> " + str(longitud))
cadena_dos = "hola como estan"
print(" Total de letras en la cadena 2 es ---> " + str(len(cadena_dos)))


