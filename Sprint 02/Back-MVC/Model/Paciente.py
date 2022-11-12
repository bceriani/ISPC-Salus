class UsuarioPaciente():
    #VARIABLES O CAMPOS
    __dniU = 0
    __nombre = "SIN DATO"
    __apellido = "SIN DATO"
    __telefono = "SIN DATO"
    __obraSocial = "SIN DATO"
    __medicoCabecera = 0

    #CONSTRUCTOR
    def __init__(self, nD=0, n="SIN DATO", a="SIN DATO", t="SIN DATO", oS="SIN DATO", mC=0):
        self.dniU = nD
        self.nombre = n
        self.apellido = a
        self.telefono = t
        self.obraSocial = oS
        self.medicoCabecera = mC
    #METODOS GETS
    def get_DniU(self):
        return self.dniU
    def get_Nombre(self):
        return self.nombre
    def get_Apellido(self):
        return self.apellido
    def get_Telefono(self):
        return self.telefono
    def get_ObraSocial(self):
        return self.obraSocial
    def get_MedicoCabecera(self):
        return self.medicoCabecera

    # METODOS SETS
    def set_DniU(self, nD):
        self.dniU = nD
    def set_Nombre(self, n):
        self.nombre = n
    def set_Apellido(self, a):
        self.apellido = a
    def set_Telefono(self, t):
        self.telefono = t
    def set_ObraSocial(self, oS):
        self.obraSocial = oS
    def set_MedicoCabecera(self, mC):
        self.medicoCabecera = mC

    #METODO __str__
    def __str__(self):
        cadena = str(self.dniU)+", "+self.nombre+", "+self.apellido+", "+self.telefono+", "+self.obraSocial+", "+str(self.medicoCabecera)
        return cadena

    #METODOS MOSTRAR Y CARGAR
    def cargar(self):
        self.dniU = int(input("DNI USUARIO: "))
        self.nombre = input("NOMBRE: ")
        self.apellido = input("APELLIDO: ")
        self.telefono = input("TELEFONO: ")
        self.obraSocial = input("OBRA SOCIAL: ")
        self.medicoCabecera = int(input("MEDICO CABECERA: "))
    def mostrar(self):
        print("DNI USUARIO: ", self.dniU)
        print("NOMBRE: ", self.nombre)
        print("APELLIDO: ", self.apellido)
        print("TELEFONO: ", self.telefono)
        print("OBRA SOCIAL: ", self.obraSocial)
        print("MEDICO CABECERA: ", self.medicoCabecera)