from conexion import obtener_conexion
import sqlite3

def insertar_producto(nombre, precio, inventario):
    """Inserta un nuevo producto en la tabla."""
    conexion = obtener_conexion()
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO productos (nombre, precio, inventario) VALUES (?, ?, ?)",
            (nombre, precio, inventario)
        )
        conexion.commit()
        return True
    except sqlite3.Error:
        conexion.rollback()
        return False
    finally:
        cursor.close()
        conexion.close()

def editar_producto(id, n_nombre):
    """Editar Prouducto"""
    conexion = obtener_conexion()
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE productos SET nombre = ? WHERE id = ?",
            (n_nombre, id)
        )
        conexion.commit()
        return True
    except sqlite3.Error:
        conexion.rollback()
        return False
    finally:
        cursor.close()
        conexion.close()

def eliminar_producto(id):
    """Eliminar Producto explicado"""
    conexion = obtener_conexion()
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "DELETE FROM productos WHERE id = ?",
            (id,)
        )
        conexion.commit()
        return True
    except sqlite3.Error:
        conexion.rollback()
        return False
    finally:
        cursor.close()
        conexion.close()

def obtener_todos_los_productos():
    """Recupera la lista completa de productos."""
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, precio, inventario FROM productos")
    productos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return productos
