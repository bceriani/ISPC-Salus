#ModificarEstudio()

import sqlite3

miConexion = sqlite3.connect("Salus")

miCursor = miConexion.cursor()

miCursor.execute("UPDATE EstudiosMedicos SET Paciente=5 WHERE IdEm=1")

miConexion.commit()
miCursor.close()