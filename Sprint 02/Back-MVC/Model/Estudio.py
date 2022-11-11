import datetime
#date.datetime.now() devuelve fecha de sistema en formato anio-mes-dia

#CLASE ESTUDIO
class Estudio:
    #VARIABLES O CAMPOS
    __ID_EM = 0
    __tipo = "SIN DATO"
    __fecha = datetime.datetime.now()
    __paciente = 0
    __medicoSolicitante = 0
    __ubicacion = "SIN DATO"

    #CONSTRUCTOR
    def __init__(self,id=0, t="SIN DATO", f=datetime.datetime.now(), p=0, ms=0, u="SIN DATO"):
        self.ID_EM = id
        self.tipo = t
        self.fecha = f
        self.paciente = p
        self.medicoSolicitante = ms
        self.ubicacion = u
    #METODOS GETS
    def get_ID_EM(self):
        return self.ID_EM
    def get_Tipo(self):
        return self.tipo
    def get_Fecha(self):
        return self.fecha
    def get_Paciente(self):
        return self.paciente
    def get_MedicoSolicitante(self):
        return self.medicoSolicitante
    def get_Ubicacion(self):
        return self.ubicacion

    #METODOS SETS
    def set_ID_EM(self, id):
        self.ID_EM = id
    def set_Tipo(self, t):
        self.tipo = t
    def set_Fecha(self, f):
        self.fecha = f
    def set_Paciente(self, p):
        self.paciente = p
    def set_MedicoSolicitante(self, ms):
        self.medicoSolicitante = ms
    def set_Ubicacion(self, u):
        self.ubicacion = u

    #METODO __str__
    def __str__(self):
        cadena = str(self.ID_EM)+", "+self.tipo+", "+str(self.fecha)+", "+str(self.paciente)+", "+str(self.medicoSolicitante)+", "+self.ubicacion
        return cadena
    #METODOS MOSTRAR Y CARGAR
    def cargar(self):
        self.ID_EM = int(input("ID-EM: "))
        self.tipo = input("TIPO: ")
        self.fecha = input("FECHA: ")
        self.paciente = int(input("PACIENTE: "))
        self.medicoSolicitante = int(input("MEDICO SOLICITANTE: "))
        self.ubicacion = input("UBICACION: ")
    def mostrar(self):
        print("ID-EM: ",self.ID_EM)
        print("TIPO: ", self.tipo)
        print("FECHA: ", self.fecha)
        print("PACIENTE: ", self.paciente)
        print("MEDICO SOLICITANTE: ", self.medicoSolicitante)
        print("UBICACION: ", self.ubicacion)
