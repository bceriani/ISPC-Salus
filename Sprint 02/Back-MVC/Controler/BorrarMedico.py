#BorrarMedico()

import sqlite3
miConexion = sqlite3.connect("Salus")
miCursor = miConexion.cursor()
miCursor.execute("""
        CREATE TABLE if not exists UsuarioMedico (
        DniM integer Primary key not null,
        Matricula integer not null,
        Nombre varchar (45) not null,
        Apellido  varchar (45) not null,
        Telefono varchar (45) not null,
        Celular varchar (45) not null,
        Localidad varchar (45) not null,
        Email varchar (45) not null
        )
""")

miCursor.execute("DELETE FROM UsuarioMedico WHERE DniM = 222222222")
miConexion.commit()
miConexion.close()