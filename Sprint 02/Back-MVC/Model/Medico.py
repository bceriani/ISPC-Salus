class Medico():
    #VARIABLES O CAMPOS
    __DNI = 0
    __ID_M = 0
    __matricula = 0
    __especialidad = "SIN DATO"
    __nombre = "SIN DATO"
    __apellido = "SIN DATO"
    __telefono = "SIN DATO"
    __celular = "SIN DATO"
    __localidad = "SIN DATO"
    __email = "SIN DATO"

    #CONSTRUCTOR
    def __init__(self, nD=0, idM=0, m=0, e="SIN DATO", n="SIN DATO", a="SIN DATO", t="SIN DATO", c="SIN DATO", l="SIN DATO", eM="SIN DATO"):
        self.DNI = nD
        self.ID_M = idM
        self.matricula = m
        self.especialidad = e
        self.nombre = n
        self.apellido = a
        self.telefono = t
        self.celular = c
        self.localidad = l
        self.email = eM

    #METODOS GETS
    def get_DNI(self):
        return self.DNI
    def get_ID_M(self):
        return self.ID_M
    def get_Matricula(self):
        return self.matricula
    def get_Especialidad(self):
        return self.especialidad
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
    def set_DNI(self, nD):
        self.DNI = nD
    def set_ID_M(self, idM):
        self.ID_M = idM
    def set_Matricula(self, m):
        self.matricula = m
    def set_Especialidad(self, e):
        self.especialidad = e
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
        cadena = str(self.DNI)+", "+str(self.ID_M)+", "+str(self.matricula)+", "+self.especialidad+", "+self.nombre+", "+self.apellido+", "+self.telefono+", "+self.celular+", "+self.localidad+", "+self.email
        return cadena

    #METODOS MOSTRAR Y CARGAR
    def cargar(self):
        self.DNI = int(input("DNI: "))
        self.ID_M = int(input("ID_M: "))
        self.matricula = int(input("MATRICULA: "))
        self.especialidad = input("ESPECIALIDAD: ")
        self.nombre = input("NOMBRE: ")
        self.apellido = input("APELLIDO: ")
        self.telefono = input("TELEFONO: ")
        self.celular = input("CELULAR: ")
        self.localidad = input("LOCALIDAD: ")
        self.email = input("EMAIL: ")
    def cargar(self):
        print("DNI: ", self.DNI)
        print("ID_M: ", self.ID_M)
        print("MATRICULA: ", self.matricula))
        print("ESPECIALIDAD: ", self.especialidad)
        print("NOMBRE: ", self.nombre)
        print("APELLIDO: ", self.apellido)
        print("TELEFONO: ", self.telefono)
        print("CELULAR: ", self.celular)
        print("LOCALIDAD: ", self.localidad)
        print("EMAIL: ", self.email)