from Config.database_connection import create_connection
from mysql.connector import Error

class EstudianteController:
    @staticmethod
    def obtener_materias_asignadas(id_estudiante):
        """Obtiene las materias en las que está inscrito un estudiante."""
        conexion = create_connection()
        if conexion:
            try:
                cursor = conexion.cursor(dictionary=True)
                query = """
                SELECT m.id, m.nombre, m.descripcion
                FROM materias m
                INNER JOIN inscripciones i ON m.id = i.id_materia
                WHERE i.id_estudiante = %s
                """
                cursor.execute(query, (id_estudiante,))
                materias = cursor.fetchall()
                return materias
            except Error as e:
                print(f"Error al obtener materias asignadas: {e}")
                return []
            finally:
                cursor.close()
                conexion.close()

    @staticmethod
    def obtener_calificaciones(id_estudiante):
        """Obtiene las calificaciones del estudiante en sus materias."""
        conexion = create_connection()
        if conexion:
            try:
                cursor = conexion.cursor(dictionary=True)
                query = """
                SELECT m.nombre AS materia, n.nota
                FROM notas n
                INNER JOIN materias m ON n.id_materia = m.id
                WHERE n.id_estudiante = %s
                """
                cursor.execute(query, (id_estudiante,))
                calificaciones = cursor.fetchall()
                return calificaciones
            except Error as e:
                print(f"Error al obtener calificaciones: {e}")
                return []
            finally:
                cursor.close()
                conexion.close()

    @staticmethod
    def obtener_detalle_materia(id_estudiante, id_materia):
        """Obtiene los detalles de una materia específica en la que está inscrito el estudiante."""
        conexion = create_connection()
        if conexion:
            try:
                cursor = conexion.cursor(dictionary=True)
                query = """
                SELECT m.id, m.nombre, m.descripcion, p.nombre AS profesor
                FROM materias m
                INNER JOIN asignaciones a ON m.id = a.id_materia
                INNER JOIN profesores p ON a.id_profesor = p.id
                INNER JOIN inscripciones i ON m.id = i.id_materia
                WHERE i.id_estudiante = %s AND m.id = %s
                """
                cursor.execute(query, (id_estudiante, id_materia))
                detalle = cursor.fetchone()
                return detalle
            except Error as e:
                print(f"Error al obtener detalle de la materia: {e}")
                return None
            finally:
                cursor.close()
                conexion.close()

    @staticmethod
    def obtener_promedio_general(id_estudiante):
        """Calcula el promedio general de las calificaciones del estudiante."""
        conexion = create_connection()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = """
                SELECT AVG(nota) AS promedio
                FROM notas
                WHERE id_estudiante = %s
                """
                cursor.execute(query, (id_estudiante,))
                resultado = cursor.fetchone()
                return resultado['promedio'] if resultado else None
            except Error as e:
                print(f"Error al calcular promedio general: {e}")
                return None
            finally:
                cursor.close()
                conexion.close()

    @staticmethod
    def obtener_notificaciones(id_estudiante):
        """Obtiene las notificaciones enviadas al estudiante."""
        conexion = create_connection()
        if conexion:
            try:
                cursor = conexion.cursor(dictionary=True)
                query = """
                SELECT n.id, n.titulo, n.mensaje, n.fecha
                FROM notificaciones n
                WHERE n.id_estudiante = %s
                ORDER BY n.fecha DESC
                """
                cursor.execute(query, (id_estudiante,))
                notificaciones = cursor.fetchall()
                return notificaciones
            except Error as e:
                print(f"Error al obtener notificaciones: {e}")
                return []
            finally:
                cursor.close()
                conexion.close()