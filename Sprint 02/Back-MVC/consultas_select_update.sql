
/*CONSULTA USANDO UPDATE*/

UPDATE UsuarioMedico SET Nombre = Carlos_Albaro WHERE localidad = SanJusto;
UPDATE UsuarioPaciente SET ObraSocial='SWIS MEDICA' WHERE apellido = Rios_Aguirre;
UPDATE EstudioMedico SET fecha='2022/02/23'WHERE paciente= JulianMarquez;


/*CONSULTA USANDO JOIN*/

SELECT * 
FROM EstudioMedico  
INNER JOIN UsuarioPaciente ON MedicoSolicitante_id=MedicodeCabecera_id


