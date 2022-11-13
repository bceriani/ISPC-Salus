#MCargarEstudio()
import sqlite3
"""
ESTAS SON PRUEBAS FALLIDAS PARA LLAMAR A LA CLASE (MODELO) Estudio
import sys
from ../Model import Estudio
sys.path.append(0, "C:/Users/Esteban/Desktop/Model")
import Estudio
estudio1 = Estudio()
printt(estudio1)
Paciente y MedicoSolicitante son claves foraneas
"""
miConexion = sqlite3.connect("Salus")
miCursor = miConexion.cursor()
miCursor.execute("""
        CREATE TABLE if not exists EstudiosMedicos (
        IdEm integer Primary key autoincrement,
        Tipo varchar (45) not null,
        Fecha date not null,
        Paciente integer not null,
        MedicoSolicitante integer not null,
        Ubicacion varchar (150))
""")
#Aca se cargaria una instancia de la clase Estudio
#estudios = Estudio()
#estudios.cargar()
estudios = [
    ("RAYOSX", 2022, 1, 1, "Mi Ciudad"),
    ("RAYOSX2", 2022, 2, 2, "Mi Ciudad2"),
    ("RAYOSX3", 2022, 3, 3, "Mi Ciudad3"),
    ("RAYOSX4", 2022, 4, 4, "Mi Ciudad4")
]
miCursor.executemany("INSERT INTO EstudiosMedicos VALUES (NULL, ?, ?, ?, ?, ?)", estudios)
miCursor.execute("INSERT INTO EstudiosMedicos VALUES (NULL, 'RAYOSX5', '2022-11-14', 5, 5, 'Mi Ciudad5')")
miConexion.commit()
miConexion.close()