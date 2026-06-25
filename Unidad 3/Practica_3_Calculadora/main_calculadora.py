import conexion_calculadora
import calculadora_controller


class Calculadora:

    def __init__ (self):
        self.historial = []
    
    def sumar (self,a,b):
        res= a+b
        
        return res  
    
    def restar (self,a,b):
        res= a-b
        
        return res
    
    def multiplicar(self,a,b):
        res =a*b
        
        return res

    

calc = Calculadora()

def menu():
    conexion_calculadora.inicializar_base_datos()
    
    while True:

        print("\n=== Menu de calculadora ===")
        print("1. Suma")
        print("2. Resta")
        print("3. Producto")
        print("4. Historial")
        print("5. Salir")

        op = input("Selecciona una opción: ")

        if op == "1":
            suma()
        elif op == "2":
            resta()
        elif op == "3":
            producto()
        elif op == "4":
            historial()
        elif op == "5":
            print("Saliendo de la calculadora")
            break
        else:
            print("Selecciona una opcíon valida")


#### Funciones del menu #####

def suma():
    
    num_a = int(input("Ingrese el valor de a:  ")) 
    num_b = int(input("Ingrese el valor de b:  ")) 
    print (f"El resultado de la suma es: {calc.sumar(num_a,num_b)}")

    exito = calculadora_controller.set_operaciones(num_a, '+', num_b, calc.sumar(num_a,num_b))
    if exito:
        print("¡operación guardada!")
    else:
        print("Error al guardar el la operación.")

def resta():
    num_a = int(input("Ingrese el valor de a:  ")) 
    num_b = int(input("Ingrese el valor de b:  ")) 
    print (f"El resultado de la resta es: {calc.restar(num_a,num_b)}")

    exito = calculadora_controller.set_operaciones(num_a, '-', num_b, calc.restar(num_a,num_b))
    if exito:
        print("¡operación guardada!")
    else:
        print("Error al guardar el la operación.")

def producto():
    num_a = int(input("Ingrese el valor de a:  ")) 
    num_b = int(input("Ingrese el valor de b:  ")) 
    print (f"El resultado de la multiplicación es: {calc.multiplicar(num_a,num_b)}")

    exito = calculadora_controller.set_operaciones(num_a, 'X', num_b, calc.multiplicar(num_a,num_b))
    if exito:
        print("¡operación guardada!")
    else:
        print("Error al guardar el la operación.")
    
def historial():
    operaciones = calculadora_controller.get_operaciones()
    print("\n--- Operaciones realizadas ---")
    for o in operaciones:
        print(f" {o[0]} {o[1]} {o[2]} = {o[3]}")

# Punto de entrada único del programa
if __name__ == "__main__":
    menu()