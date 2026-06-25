import sqlite3

DATABASE_NAME = "cal_bd.db"

def obtener_conexion():
    """Devuelve un objeto de conexión listo para usar."""
    return sqlite3.connect(DATABASE_NAME)

def inicializar_base_datos():
    """Crea las tablas necesarias si no existen."""
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS operaciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            num_a INTEGER NOT NULL,
            symbol TEXT NOT NULL,
            num_b INTEGER NOT NULL,
            resultado INTEGER NOT NULL
        )
    """)
    conexion.commit()
    cursor.close()
    conexion.close()

# Si ejecutas este archivo por error, inicializa la BD
if __name__ == "__main__":
    inicializar_base_datos()
    print("Se creo la base de datos de la calculadora")
