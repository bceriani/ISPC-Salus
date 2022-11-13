class UsuarioMedico():
    #VARIABLES O CAMPOS
    __dniM = 0
    __matricula = 0
    __nombre = "SIN DATO"
    __apellido = "SIN DATO"
    __telefono = "SIN DATO"
    __celular = "SIN DATO"
    __localidad = "SIN DATO"
    __email = "SIN DATO"

    #CONSTRUCTOR
    def __init__(self, nD=0, idM=0, n="SIN DATO", a="SIN DATO", t="SIN DATO", c="SIN DATO", l="SIN DATO", eM="SIN DATO"):
        self.dniM = nD
        self.matricula = idM
        self.nombre = n
        self.apellido = a
        self.telefono = t
        self.celular = c
        self.localidad = l
        self.email = eM

    #METODOS GETS
    def get_DniM(self):
        return self.dniM
    def get_Matricula(self):
        return self.matricula
    def get_Nombre(self):
        return self.nombre
    def get_Apellido(self):
        return self.apellido
    def get_Telefono(self):
        return self.telefono
    def get_Celuldar(self):
        return self.celular
    def get_Localidad(self):
        return self.localidad
    def get_Email(self):
        return self.email

    # METODOS SETS
    def set_DniM(self, nD):
        self.dniM = nD
    def set_Matricula(self, m):
        self.matricula = m
    def set_Nombre(self, n):
        self.nombre = n
    def set_Apellido(self, a):
        self.apellido = a
    def set_Telefono(self, t):
        self.telefono = t
    def set_Celuldar(self, c):
        self.celular = c
    def set_Localidad(self, l):
        self.localidad = l
    def set_Email(self, eM):
        self.email = eM

    #METODO __str__
    def __str__(self):
        cadena = str(self.dniM)+", "+str(self.matricula)+", "+self.nombre+", "+self.apellido+", "+self.telefono+", "+self.celular+", "+self.localidad+", "+self.email
        return cadena

    #METODOS MOSTRAR Y CARGAR
    def cargar(self):
        self.dniM = int(input("DNI MEDICO: "))
        self.matricula = int(input("MATRICULA: "))
        self.nombre = input("NOMBRE: ")
        self.apellido = input("APELLIDO: ")
        self.telefono = input("TELEFONO: ")
        self.celular = input("CELULAR: ")
        self.localidad = input("LOCALIDAD: ")
        self.email = input("EMAIL: ")
    def mostrar(self):
        print("DNI MEDICO: ", self.dniM)
        print("MATRICULA: ", self.matricula)
        print("NOMBRE: ", self.nombre)
        print("APELLIDO: ", self.apellido)
        print("TELEFONO: ", self.telefono)
        print("CELULAR: ", self.celular)
        print("LOCALIDAD: ", self.localidad)
        print("EMAIL: ", self.email)