drop database if exists Salus;
create database Salus;
use Salus;
create table UsuarioMedico (
	DniM int(8) not null primary key,
	Matricula int(8) not null,
	Nombre varchar(45) not null,
	Apellido varchar(45) not null,
	Telefono varchar(45) not null,
	Celular varchar(45) not null,
	Localidad varchar(45) not null,
	Email varchar(45) not null
);
create table UsuarioPaciente(
	DniU int(8) not null primary key,
	Nombre varchar(45) not null,
	Apellido varchar(45) not null,
	Telefono varchar(45) not null,
	ObraSocial varchar(45) not null,
	MedicoDeCabecera  int
);

create table EstudiosMedicos (
	IdEm int not null auto_increment,
    Tipo varchar(45) not null,
    Fecha date not null,
    Paciente int not null,
    MedicoSolicitante int not null,
    Ubicacion varchar(150),
    primary key(IdEm),
    
  
    foreign key (Paciente) references UsuarioPaciente(DniU),
    foreign key (MedicoSolicitante) references UsuarioMedico(DniM)
    
    );