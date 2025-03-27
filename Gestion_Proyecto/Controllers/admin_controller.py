from Config.database_connection import create_connection
from mysql.connector import Error

class AdminController:
    @staticmethod
    def obtener_usuarios():
        """Obtiene todos los usuarios del sistema."""
        conexion = create_connection()
        if conexion:
            try:
                cursor = conexion.cursor(dictionary=True)
                query = "SELECT * FROM usuarios"
                cursor.execute(query)
                usuarios = cursor.fetchall()
                return usuarios
            except Error as e:
                print(f"Error al obtener usuarios: {e}")
                return []
            finally:
                cursor.close()
                conexion.close()

    @staticmethod
    def agregar_usuario(nombre, correo, contraseña, rol):
        """Agrega un nuevo usuario al sistema."""
        conexion = create_connection()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = """
                INSERT INTO usuarios (nombre, correo, contraseña, rol)
                VALUES (%s, %s, %s, %s)
                """
                cursor.execute(query, (nombre, correo, contraseña, rol))
                conexion.commit()
                print("Usuario agregado correctamente.")
            except Error as e:
                print(f"Error al agregar usuario: {e}")
            finally:
                cursor.close()
                conexion.close()

    @staticmethod
    def eliminar_usuario(id_usuario):
        """Elimina un usuario del sistema por su ID."""
        conexion = create_connection()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "DELETE FROM usuarios WHERE id = %s"
                cursor.execute(query, (id_usuario,))
                conexion.commit()
                print("Usuario eliminado correctamente.")
            except Error as e:
                print(f"Error al eliminar usuario: {e}")
            finally:
                cursor.close()
                conexion.close()

    @staticmethod
    def actualizar_usuario(id_usuario, nombre=None, correo=None, contraseña=None, rol=None):
        """Actualiza la información de un usuario."""
        conexion = create_connection()
        if conexion:
            try:
                cursor = conexion.cursor()
                campos = []
                valores = []

                if nombre:
                    campos.append("nombre = %s")
                    valores.append(nombre)
                if correo:
                    campos.append("correo = %s")
                    valores.append(correo)
                if contraseña:
                    campos.append("contraseña = %s")
                    valores.append(contraseña)
                if rol:
                    campos.append("rol = %s")
                    valores.append(rol)

                valores.append(id_usuario)
                query = f"UPDATE usuarios SET {', '.join(campos)} WHERE id = %s"
                cursor.execute(query, valores)
                conexion.commit()
                print("Usuario actualizado correctamente.")
            except Error as e:
                print(f"Error al actualizar usuario: {e}")
            finally:
                cursor.close()
                conexion.close()

    @staticmethod
    def obtener_usuarios_con_roles():
        """Obtiene todos los usuarios con su ID, nombre y rol."""
        conexion = create_connection()
        if conexion:
            try:
                cursor = conexion.cursor(dictionary=True)
                query = "SELECT id, nombre, rol FROM usuarios"
                cursor.execute(query)
                usuarios = cursor.fetchall()
                return usuarios
            except Error as e:
                print(f"Error al obtener usuarios con roles: {e}")
                return []
            finally:
                cursor.close()
                conexion.close()