import sqlite3

def gestionar_base_datos():
    # 1. Conectar a la base de datos (se crea el archivo si no existe)
    conexion = sqlite3.connect("mi_negocio.db")
    
    try:
        # 2. Crear el objeto cursor para ejecutar comandos SQL
        cursor = conexion.cursor()
        
        # 3. Crear una tabla (con clave primaria autoincremental)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                precio REAL NOT NULL,
                inventario INTEGER DEFAULT 0
            )
        """)
        print("Tabla 'productos' creada exitosamente.")
        
        # 4. Insertar datos (usamos tuplas y marcadores '?' por seguridad)
        nuevos_productos = [
            ("Laptop", 899.99, 15),
            ("Teclado Mecánico", 75.50, 30),
            ("Ratón Inalámbrico", 25.00, 50),
            ("Monitor 4K", 349.99, 8)
        ]
        
        # ejecutemany inserta una lista completa de registros de golpe
        cursor.executemany("""
            INSERT INTO productos (nombre, precio, inventario) 
            VALUES (?, ?, ?)
        """, nuevos_productos)
        
        # ¡IMPORTANTE! Guardar los cambios en el archivo de la base de datos
        conexion.commit()
        print(f"Se insertaron {cursor.rowcount} productos con éxito.")
        
        # 5. Consultar los datos de la tabla
        print("\n--- Lista de Productos en la Base de Datos ---")
        cursor.execute("SELECT id, nombre, precio, inventario FROM productos")
        
        # Recuperamos todas las filas devueltas por la consulta
        filas = cursor.fetchall()
        
        for fila in filas:
            id_prod, nombre, precio, stock = fila
            print(f"ID: {id_prod} | {nombre} - ${precio:.2f} (Stock: {stock})")
            
    except sqlite3.Error as error:
        print(f"Ocurrió un error con la base de datos: {error}")
        # Si algo falla, deshacemos los cambios pendientes
        conexion.rollback()
        
    finally:
        # 6. Cerrar los recursos siempre al terminar
        cursor.close()
        conexion.close()
        print("\nConexión a la base de datos cerrada de forma segura.")

# Ejecutar la función
if __name__ == "__main__":
    gestionar_base_datos()
