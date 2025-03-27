from Config.database_connection import create_connection
from Models.usuario import Usuario
from Controllers.admin_controller import AdminController

class Admin(Usuario):
    def __init__(self, id=None, nombre=None, correo=None, contraseña=None):
        super().__init__(id, nombre, correo, contraseña, 'admin')

    @staticmethod
    def obtener_por_correo(correo):
        """Obtiene un administrador por su correo."""
        conexion = create_connection()
        if conexion:
            try:
                with conexion.cursor(dictionary=True) as cursor:
                    query = "SELECT * FROM administradores WHERE correo = %s"
                    cursor.execute(query, (correo,))
                    admin_data = cursor.fetchone()
                    if admin_data:
                        return Admin(
                            id=admin_data['id'],
                            nombre=admin_data['nombre'],
                            correo=admin_data['correo'],
                            contraseña=admin_data['contraseña']
                        )
            except Exception as e:
                print(f"Error al obtener administrador por correo: {e}")
            finally:
                conexion.close()
        return None

class AdminModel:
    @staticmethod
    def obtener_usuarios_con_roles():
        """Llama al controlador para obtener usuarios con ID, nombre y rol."""
        return AdminController.obtener_usuarios_con_roles()