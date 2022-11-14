#BorrarPaciente()

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

miCursor.execute("DELETE FROM UsuarioPaciente WHERE DniU = 11111111")
miConexion.commit()
miConexion.close()