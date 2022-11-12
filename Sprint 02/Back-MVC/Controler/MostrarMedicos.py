#MostrarMedico()
import sqlite3
miConexion = sqlite3.connect("Salus")
miCursor = miConexion.cursor()
miCursor.execute("Select * from UsuarioMedico where Matricula = 7")
medicos = miCursor.fetchall()
print(medicos)
miConexion.commit()
miConexion.close()