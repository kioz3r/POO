 # Ejercicio en el cual, un alumno, puede agregar n cantidad de materias 
 # y sacar el promedio de las mismas 

materias = input("Ingresa el numero de materias a capturar :")
suma = 0

for i in range(int(materias)):
    cal = input (f"Ingresa calificacion {i+1}: ")
    suma = suma + int(cal)

promedio = suma / int(materias)
print(f" Su promedio es --->", str(promedio))


