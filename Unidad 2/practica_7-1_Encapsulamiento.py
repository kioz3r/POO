class Termometro:
    def __init__(self, temperatura=0):
        self.__temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, valor): # Setter con validación
        if valor < -273.15:
            raise ValueError ('Temperatura por debajo del cero absoluto.')
        self.__temperatura = valor

    @property
    def en_fahremheit(self): #Getter calculado
        return self.__temperatura * 9/5 +32


    def __str__(self):
        return f'{self.__temperatura}°C / {self.en_fahremheit:.1f}°F'

# Haciendo uso de la clase
t=Termometro(100)
print(t)
t.temperatura = -10
print(t)
t.temperatura = -300

