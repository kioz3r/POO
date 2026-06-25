# Ejercicio 1

nom = input("Ingresa tu nombre :")
hra = input ("Ingresa la hora :")

if (int(hra) > 12 and int(hra) < 19):
    txt = 'buenas tardes'
elif (int(hra) > 19):
    txt ='buenas noches'
else:
    txt = ' buenos dias'

print (f"Hola {nom} {txt} ")

suma = 0

for i in range(5):
 
 cal = input (f"Ingresa calificacion {i+1}: ")

 suma = suma + int(cal)

promedio = suma / 5

print ("Tu promedio es de > " + str(promedio))
 




