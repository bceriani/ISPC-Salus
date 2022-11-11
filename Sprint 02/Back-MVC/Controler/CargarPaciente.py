#CargarPaciente)
import sqlite3
miConexion = sqlite3.connect("mydb")
miCursor = miConexion.cursor()
miCursor.execute("""
        CREATE TABLE if not exists US_P (
        DNI integer Primary key autoincrement,
        Nombre varchar (45),
        Apellido varchar (45),
        Telefono  varchar (45),
        ObraSocial varchar (45),
        MedicoCabecera integer)
""")
pacientes = [
    ("Pepito", "Perez", "4895786", "PAMI", 1),
    ("Pepito2", "Perez2", "4895786", "PAMI2", 2),
    ("Pepito3", "Perez3", "4895786", "PAMI3", 3),
    ("Pepito4", "Perez4", "4895786", "PAMI4", 4)
]
miCursor.executemany("INSERT INTO US_P VALUES (NULL, ?, ?, ?, ?, ?)", pacientes)
miConexion.commit()
miConexion.close()