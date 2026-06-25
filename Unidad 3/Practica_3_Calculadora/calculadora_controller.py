from conexion_calculadora import obtener_conexion
import sqlite3

def set_operaciones(a, sym, b, res):
    conexion = obtener_conexion()
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO operaciones (num_a, symbol, num_b, resultado) VALUES (?, ?, ?, ?)",
            (a, sym, b, res)
        )
        conexion.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error de SQLite: {e}")
        conexion.rollback()
        return False
    finally:
        cursor.close()
        conexion.close()

def get_operaciones():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT num_a, symbol, num_b, resultado FROM operaciones")
    productos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return productos
