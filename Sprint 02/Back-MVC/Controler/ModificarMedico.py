#ModificarMedico()

import sqlite3

miConexion = sqlite3.connect("Salus")

miCursor = miConexion.cursor()

miCursor.execute("""
    create table if not exists UsuarioMedico (
	DniM int(8) not null primary key,
	Matricula int(8) not null,
	Nombre varchar(45) not null,
	Apellido varchar(45) not null,
	Telefono varchar(45) not null,
	Celular varchar(45) not null,
	Localidad varchar(45) not null,
	Email varchar(45) not null)
""")

miCursor.execute("INSERT INTO UsuarioMedico VALUES (12345678, 1, 'Juan', 'Pablo', '12345', '000000', 'Ciudad1', 'email1')")
#Aca se ejecuta el crud update
miCursor.execute("UPDATE UsuarioMedico SET Celular='3514576' WHERE Matricula=1")

miConexion.commit()
miCursor.close()
