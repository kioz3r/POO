
# Creando clase persona 
#===========================================================
class Persona:
    # Atributos de clase
    # Constructor y definicion de atributos
    def __init__(self, nombre, edad,especie):
        self.nombre = nombre
        self.edad = edad 
        self.especie = especie

    # Metodos de la clase persona 

    def saludar(self):
        return f'Hola mi nombre es {self.nombre}, y tengo {self.edad} años, y eres de la especie {self.especie}' 
        
    def cumpleanios(self):
        self.edad += 1
        return f'Para el proximo año tendras la edad de {self.edad} años'
    
    # Representación del objeto como texto 
    def __str__(self):
       return f'Persona ({self.nombre}, {self.edad})'
    
#===========================================================

# Haciendo uso de la clase de manera directa en los valores 
# Asignando valores desde consola y creacion de los objetos 

objeto1 = Persona('Ana', 25, 'Homo sapiens')
objeto2 = Persona('Carlos', 30, 'Homo herectus')

print(objeto1.saludar())
print(objeto2.saludar())
print(objeto1.cumpleanios())
print(objeto2.cumpleanios())
print(objeto1)

# nom1= input('Ingresa tu nombre: ')
# edad1= int(input ('Inresa la edad: '))

# obj1 = Persona (nom1,edad1)

# print(obj1.saludar())
# print(obj1.cumpleanios())



    

