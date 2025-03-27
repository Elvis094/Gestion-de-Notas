from Models.admin import Admin
from Models.profesor import Profesor
from Models.estudiante import Estudiante
from Models.padre import Padre
from Models.usuario import Usuario
from werkzeug.security import check_password_hash

class AutenticacionController:
    @staticmethod
    def login(correo, contraseña):
        # Primero verifica si el correo pertenece a un administrador
        administrador = Admin.obtener_por_correo(correo)
        if administrador and check_password_hash(administrador.contraseña, contraseña):
            return administrador
        
        # Si no es administrador, verifica en la tabla usuarios
        usuario = Usuario.obtener_por_correo(correo)
        if usuario and check_password_hash(usuario.contraseña, contraseña):
            if usuario.tipo == 'profesor':
                return Profesor(usuario.id, usuario.nombre, usuario.correo, usuario.contraseña)
            elif usuario.tipo == 'estudiante':
                return Estudiante(usuario.id, usuario.nombre, usuario.correo, usuario.contraseña)
            elif usuario.tipo == 'padre':
                return Padre(usuario.id, usuario.nombre, usuario.correo, usuario.contraseña)
        return None