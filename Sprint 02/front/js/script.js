
/// FORMULARIO CONTACTO

function onEnviar(){
    const nombres = document.querySelector('[data-form-nombres]');
    const apellidos = document.querySelector('[data-form-apellidos]');
    const email = document.querySelector('[data-form-email]');
    const mensajes = document.querySelector('[data-form-mensajes]');
    alert(nombres.value+" "+apellidos.value+" "+email.value+" "+mensajes.value+" 'llamar controlador'");
}



/// FORMMULARIO REGISTRO
function regPaciente(){
    opcion = "PACIENTE"
}

function regMedico(){
    opcion = "MEDICO"
}

function onEnviarRegistro(){
    const nombres = document.querySelector('[data-form-nombres]');
    const apellidos = document.querySelector('[data-form-apellidos]');
    const email = document.querySelector('[data-form-email]');
    const contrasenia = document.querySelector('[data-form-contrasenia]');
    alert(nombres.value+" "+apellidos.value+" "+email.value+" "+contrasenia.value+"llamar controlador "+opcion)
}

/* function onEnviarRegistro(){
    (() => {
        const paciente = document.querySelector('[data-form-paciente]');
        const medico = document.querySelector('[data-form-medico]');

        const createTaskPaciente = (evento) => {
            const nombres = document.querySelector('[data-form-nombres]');
            const apellidos = document.querySelector('[data-form-apellidos]');
            const email = document.querySelector('[data-form-email]');
            const contrasenia = document.querySelector('[data-form-contrasenia]');
            alert(nombres.value+" "+apellidos.value+" "+email.value+" "+contrasenia.value+" 'llamar controlador paciente'")
        };

        const createTaskMedico = (evento) => {
            const nombres = document.querySelector('[data-form-nombres]');
            const apellidos = document.querySelector('[data-form-apellidos]');
            const email = document.querySelector('[data-form-email]');
            const contrasenia = document.querySelector('[data-form-contrasenia]');
            alert(nombres.value+" "+apellidos.value+" "+email.value+" "+contrasenia.value+" 'llamar controlador medico'")
        };

        //Arrow functions o funciones anonimas
        paciente.addEventListener('click', createTaskPaciente);
        medico.addEventListener('click', createTaskMedico);
    })();
} */
