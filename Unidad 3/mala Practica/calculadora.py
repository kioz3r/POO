# calculadora.py

def sumar(a, b):
    return a + b

# Provocamos el accidente: una llamada de prueba suelta sin el if
if __name__ == "__main__":
    print("💥 [Calculadora]: Estoy haciendo una prueba interna...")
    resultado_prueba = sumar(2, 2)
    print(f"💥 [Calculadora]: El resultado de la prueba es {resultado_prueba}")