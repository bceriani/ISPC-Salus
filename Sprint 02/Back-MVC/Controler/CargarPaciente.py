#CargarPaciente)
import sqlite3
miConexion = sqlite3.connect("Salus")
miCursor = miConexion.cursor()
miCursor.execute("""
        CREATE TABLE if not exists UsuarioPaciente (
        DniU integer Primary key not null,
        Nombre varchar (45) not null,
        Apellido varchar (45) not null,
        Telefono  varchar (45) not null,
        ObraSocial varchar (45) not null,
        MedicoCabecera integer not null)
""")
pacientes = [
    (11111111, "Pepito", "Perez", "4895786", "PAMI", 1),
    (22222222, "Pepito2", "Perez2", "4895786", "PAMI2", 2),
    (33333333, "Pepito3", "Perez3", "4895786", "PAMI3", 3),
    (44444444,"Pepito4", "Perez4", "4895786", "PAMI4", 4)
]
miCursor.executemany("INSERT INTO UsuarioPaciente VALUES (?, ?, ?, ?, ?, ?)", pacientes)
miCursor.execute("INSERT INTO UsuarioPaciente VALUES (55555555, 'Pepito5', 'Perez5', 4895786, 'PAMI5', 5)")
miConexion.commit()
miConexion.close()