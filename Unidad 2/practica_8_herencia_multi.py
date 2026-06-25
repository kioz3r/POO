class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.velocidad = 0

    def acelerar(self, km):
        self.velocidad += km
        return f'{self.marca} {self.modelo} va a {self.velocidad} km/h'
    
    def frenar(self):
        self.velocidad = 0
        return f'{self.marca} {self.modelo} se detuvo'
    

    

class Automovil(Vehiculo): #Hereda de vehiculo 
    def __init__(self, marca, modelo, anio, num_puertas):
        super().__init__(marca, modelo, anio)
        self.num_puertas = num_puertas
    
    def encender_ac(self):
        return 'Aire acondicionado encendido.'
    

class AutoDeportivo(Automovil): #Hereda de automovil
    def __init__(self, marca, modelo, anio, turbo=True):
        super().__init__(marca, modelo, anio , 2) # hace referencia a que tiene 2 puertas
        self.turbo = turbo

    def modo_sport(self):
        return f'{self.marca} activó el modo Sport.'
    

# Haciendo uso de la clase

deportivo = AutoDeportivo ('Fierrari', 488, 2023)
print(deportivo.acelerar(100)) # Hereda de vehiculo 
print(deportivo.encender_ac()) # hereda de Automovil
print(deportivo.modo_sport()) # Propio de Auto deportivo
print(deportivo.num_puertas) # Pinta 2 por que es una propiedad que se harcodea en la misma funcion