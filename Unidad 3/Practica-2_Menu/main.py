import conexion
import consultas

def menu_principal():
    # 1. Asegurar que la base de datos exista al arrancar
    conexion.inicializar_base_datos()
    
    while True:
        print("\n=== SISTEMA DE INVENTARIO ===")
        print("1. Ver productos")
        print("2. Agregar producto")
        print("3. Editar producto ")
        print("4. Eliminar producto ")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            verProductos()
                
        elif opcion == "2":
            agregarProductos()
                
        elif opcion == "3":
            editarProductos()
    
        elif opcion == '4':
            eliminarProductos()
            
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

def verProductos():
    productos = consultas.obtener_todos_los_productos()
    print("\n--- Productos registrados ---")
    for p in productos:
        print(f"ID: {p[0]} | {p[1]} - ${p[2]:.2f} (Stock: {p[3]})")

def agregarProductos():
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    inventario = int(input("Cantidad en stock: "))        
    exito = consultas.insertar_producto(nombre, precio, inventario)
    if exito:
        print("¡Producto guardado exitosamente!")
    else:
        print("Error al guardar el producto.")

def editarProductos():
    """ Solo permite editar el nombre del producto por medio del ID"""
    productos = consultas.obtener_todos_los_productos()
    print("\n--- Selecciona el producto a editar ---")
    for p in productos:
        print(f"OP: {p[0]} | {p[1]} - ${p[2]:.2f} (Stock: {p[3]})")

        id = input("Ingresa el número del elemento a editar: ")

        print("----")

        producto = productos[int(id)-1]
        nombre_producto = producto[1]

        print(f'Opción seleccionada: {nombre_producto}')
        nombre = input("Ingrese nuevo nombre del producto : ")
        exito = consultas.editar_producto(int(id),nombre)

        if exito:
            print("¡Producto editado exitosamente!")
        else:
            print("Error al editar el producto.")

def eliminarProductos():
    
    productos = consultas.obtener_todos_los_productos()
    print("\n--- Lista de Productos ---")
        
    for p in productos:
        print(f"OP: {p[0]} | {p[1]}")
    
    id = input("Ingresa el número del elemento a eliminar: ")   
    print(f"El id a eliminar es -- {id}")
    exito = consultas.eliminar_producto(int(id))
        
    if exito:
        print("¡Producto eliminado exitosamente!")
    else:
        print("Error al eliminar producto.")



# Punto de entrada único del programa
if __name__ == "__main__":
    menu_principal()
