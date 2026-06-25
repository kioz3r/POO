
 ## ===== PRACTICAS CON CICLO FOR 

# Iteraciones con el ciclo for en rango 
for item in range (5):
    print(f" El valor del item es: ", str(item+1))

# Iteraciones con una lista 
materias = ['Matematicas','Español', 'POO']
for m in materias:
    print(f'Materia: {m}')

#Iteracion con paso
for value in range(0,11,2):
    print(f'El valor es: {value}')


## === PRACTICAS CON WHILE

# El ciclo de repite mientras la condicíon sea verdadera
contador = 0
while contador < 5:
    print(f'El valor del contador es: {contador} ')
    contador+=1


# Palabras especiales dentro de los bloques 

for i in range(10):
    if i == 3:
        continue
    if i == 7:
     break
    print(f'Valor de i: {i}')

# COLECCIONES DE DATOS
# Agregar nuevos elementos a una lista 

lista = ['manzana','pera','uva']
for i in lista:
    print(f'Nombre del delemento en la lista: {i}')

lista.append('melon')

for i in lista:
    print(f'Nuevos elementos en lista: {i}')

lista.insert(2,'Sandia')
print(f'Nueva lista: {lista}')

# Removiendo elemento con pop

lista.pop(2)
print(f'Elemento eliminado de la lista: {lista}')

# ordenando de manera alfabética los elementos de la lista
lista.sort()
print(f'ordenamiento con sort: {lista}')
lista.sort(reverse=True)
print(f'ordenamiento con sort(reverse=True): {lista}')