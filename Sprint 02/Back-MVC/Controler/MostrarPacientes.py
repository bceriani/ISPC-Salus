#MostrarPaciente)
import sqlite3
miConexion = sqlite3.connect("Salus")
miCursor = miConexion.cursor()
miCursor.execute("Select * from UsuarioPaciente where DniU = 33333333")
pacientes = miCursor.fetchall()
print(pacientes)
miConexion.commit()
miConexion.close()