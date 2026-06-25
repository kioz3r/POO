import sqlite3

DATABASE_NAME = "base_dos.db"

def obtener_conexion():
    """Devuelve un objeto de conexión listo para usar."""
    return sqlite3.connect(DATABASE_NAME)

def inicializar_base_datos():
    """Crea las tablas necesarias si no existen."""
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            inventario INTEGER DEFAULT 0
        )
    """)
    conexion.commit()
    cursor.close()
    conexion.close()

# Si ejecutas este archivo por error, inicializa la BD
if __name__ == "__main__":
    inicializar_base_datos()
    print("Base de datos inicializada correctamente.")
