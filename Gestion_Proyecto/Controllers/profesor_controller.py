from Config.database_connection import create_connection
from mysql.connector import Error

class ProfesorController:
    @staticmethod
    def obtener_materias_asignadas(id_profesor):
        """Obtiene las materias asignadas a un profesor."""
        conexion = create_connection()
        if conexion:
            try:
                cursor = conexion.cursor(dictionary=True)
                query = """
                SELECT m.id, m.nombre 
                FROM materias m
                INNER JOIN asignaciones a ON m.id = a.id_materia
                WHERE a.id_profesor = %s
                """
                cursor.execute(query, (id_profesor,))
                materias = cursor.fetchall()
                return materias
            except Error as e:
                print(f"Error al obtener materias asignadas: {e}")
                return []
            finally:
                cursor.close()
                conexion.close()

    @staticmethod
    def obtener_estudiantes_por_materia(id_materia):
        """Obtiene los estudiantes inscritos en una materia específica."""
        conexion = create_connection()
        if conexion:
            try:
                cursor = conexion.cursor(dictionary=True)
                query = """
                SELECT e.id, e.nombre, e.correo 
                FROM estudiantes e
                INNER JOIN inscripciones i ON e.id = i.id_estudiante
                WHERE i.id_materia = %s
                """
                cursor.execute(query, (id_materia,))
                estudiantes = cursor.fetchall()
                return estudiantes
            except Error as e:
                print(f"Error al obtener estudiantes por materia: {e}")
                return []
            finally:
                cursor.close()
                conexion.close()

    @staticmethod
    def asignar_nota(id_estudiante, id_materia, nota):
        """Asigna o actualiza una nota para un estudiante en una materia específica."""
        conexion = create_connection()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = """
                INSERT INTO notas (id_estudiante, id_materia, nota)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE nota = %s
                """
                cursor.execute(query, (id_estudiante, id_materia, nota, nota))
                conexion.commit()
                print("Nota asignada correctamente.")
            except Error as e:
                print(f"Error al asignar nota: {e}")
            finally:
                cursor.close()
                conexion.close()

    @staticmethod
    def cambiar_nota(id_estudiante, id_materia, nueva_nota):
        """Cambia la nota de un estudiante en una materia específica."""
        conexion = create_connection()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "UPDATE notas SET nota = %s WHERE id_estudiante = %s AND id_materia = %s"
                cursor.execute(query, (nueva_nota, id_estudiante, id_materia))
                conexion.commit()
                print("Nota cambiada correctamente.")
            except Error as e:
                print(f"Error al cambiar nota: {e}")
            finally:
                cursor.close()
                conexion.close()

    @staticmethod
    def enviar_notificacion(correo, asunto, mensaje):
        """Envía una notificación por correo electrónico a un estudiante."""
        # Aquí puedes usar una librería como smtplib para enviar correos electrónicos.
        try:
            print(f"Enviando correo a {correo}...")
            print(f"Asunto: {asunto}")
            print(f"Mensaje: {mensaje}")
            # Lógica para enviar correo (smtplib, etc.)
            print("Correo enviado correctamente.")
        except Exception as e:
            print(f"Error al enviar correo: {e}")

    @staticmethod
    def notificar_cambio_nota(id_estudiante, id_materia, nueva_nota):
        """Notifica al estudiante sobre el cambio de su nota."""
        conexion = create_connection()
        if conexion:
            try:
                cursor = conexion.cursor(dictionary=True)
                # Obtener información del estudiante y la materia
                query = """
                SELECT e.correo, e.nombre AS estudiante, m.nombre AS materia
                FROM estudiantes e
                INNER JOIN inscripciones i ON e.id = i.id_estudiante
                INNER JOIN materias m ON i.id_materia = m.id
                WHERE e.id = %s AND m.id = %s
                """
                cursor.execute(query, (id_estudiante, id_materia))
                resultado = cursor.fetchone()

                if resultado:
                    correo = resultado['correo']
                    estudiante = resultado['estudiante']
                    materia = resultado['materia']
                    asunto = "Cambio de Nota"
                    mensaje = f"Hola {estudiante},\n\nTu nota en la materia '{materia}' ha sido actualizada a: {nueva_nota}.\n\nSaludos."
                    ProfesorController.enviar_notificacion(correo, asunto, mensaje)
                else:
                    print("No se encontró información del estudiante o la materia.")
            except Error as e:
                print(f"Error al notificar cambio de nota: {e}")
            finally:
                cursor.close()
                conexion.close()