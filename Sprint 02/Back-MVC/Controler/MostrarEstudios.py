#MostrarEstudio()
import sqlite3
miConexion = sqlite3.connect("Salus")
miCursor = miConexion.cursor()
miCursor.execute("Select * from EstudiosMedicos where Fecha = '2022-11-14'")
estudios = miCursor.fetchall()
print(estudios)
miConexion.commit()
miConexion.close()