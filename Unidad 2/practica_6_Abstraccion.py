from abc import ABC, abstractmethod
import math

# Clase abstracta : define que debe hacer cada figura 
class Figura(ABC):

    @abstractmethod
    def area(self):
        pass # no hace nada pero sirve de rrelleno para evitar errores de sintaxis

    @abstractmethod
    def perimetro(self):
        pass

    #Metodo concretro : disponible para todas las figuras
    def describir(self):
               return (f'{self.__class__.__name__}: '
                f'área={self.area():.2f}, '
                f'perímetro={self.perimetro():.2f}')
    

#Clase concreta: Implementa los metodos abstractos de la clase FIGURA
class Circulo(Figura):
      def __init__(self, radio):
            self.radio = radio

      def area(self):
            return math.pi * self.radio ** 2
      
      def perimetro(self):
            return 2 * math.pi * self.radio
      

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base   = base
        self.altura = altura
 
    def area(self):
        return self.base * self.altura
 
    def perimetro(self):
        return 2 * (self.base + self.altura)


class Triangulo(Figura):
        def __init__(self, a, b, c):
            self.a, self.b, self.c = a, b, c
 
        def area(self):
            s = (self.a + self.b + self.c) / 2   # Semiperímetro
            return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
 
        def perimetro(self):
            return self.a + self.b + self.c
        

# --- Usando las Clases ---
figuras = [Circulo(5), Rectangulo(4, 6), Triangulo(3, 4, 5)]
 
for figura in figuras:
    print(figura.describir())
 


