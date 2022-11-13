#ModificarPaciente()

import sqlite3

miConexion = sqlite3.connect("Salus")

miCursor = miConexion.cursor()

miCursor.execute("UPDATE UsuarioPaciente SET ObraSocial='MEDIFE' WHERE DniU=11111111")

miConexion.commit()
miCursor.close()