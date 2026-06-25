class Calculadora:

    def __init__ (self, marca):
        self.marca = marca
        self.historial = []
     
    def sumar (self,a,b):
        res= a+b
        self.historial.append(f'{a} + {b} = {res}')  
        return res  
    
    def restar (self,a,b):
        res= a-b
        self.historial.append(f'{a} - {b} = {res}')  
        return res
    
    def multiplicar(self,a,b):
        res =a*b
        self.historial.append(f'{a} x {b} = {res}')  
        return res
    
    def ver_historial(self):
        print (f'------- Historial de la calculadora {self.marca}')
        for op in self.historial:
            print('  ', op)
    
# Haciendo uso de la clase 
calc = Calculadora('Casio')
print(calc.sumar(10,5))
print(calc.restar(20,8))
print(calc.multiplicar(3,7))
calc.ver_historial()
