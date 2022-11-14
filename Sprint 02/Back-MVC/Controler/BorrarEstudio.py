#BorrarMedico()

import sqlite3
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

miCursor.execute("DELETE FROM EstudiosMedicos WHERE IdEm = 1")
miConexion.commit()
miConexion.close()