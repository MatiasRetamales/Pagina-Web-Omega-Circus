// Selecciona el formulario usando su clase
const formulario = document.querySelector('.contacto-formulario');

// Añade un evento 'submit' al formulario
formulario.addEventListener('submit', function(event) {
    // Muestra un cuadro de confirmación
    const confirmacion = window.confirm("¿Estás seguro de que quieres enviar el formulario?");
    
    // Si el usuario cancela, prevenimos el envío del formulario
    if (!confirmacion) {
        event.preventDefault();
    }
});
