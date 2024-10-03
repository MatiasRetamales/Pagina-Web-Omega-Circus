// Espera a que el DOM se cargue completamente antes de ejecutar el script
document.addEventListener('DOMContentLoaded', function() {
    // Selecciona todas las imágenes dentro de la galería
    var imagenes = document.querySelectorAll('.galeria img');

    // Selecciona el contenedor de la imagen ampliada y el elemento de la imagen
    var imagenAmpliada = document.getElementById('imagen-ampliada');
    var imgAmpliada = document.getElementById('imagen-ampliada-src');

    // Añade un evento de clic a cada imagen de la galería
    imagenes.forEach(function(imagen) {
        imagen.addEventListener('click', function() {
            // Obtiene la fuente de la imagen clicada
            var src = imagen.src;

            // Muestra el contenedor de la imagen ampliada y actualiza la fuente de la imagen
            imagenAmpliada.style.display = 'flex';
            imgAmpliada.src = src;
        });
    });

    // Añade un evento de clic al área de cierre para ocultar la imagen ampliada
    document.getElementById('cerrar').addEventListener('click', function() {
        imagenAmpliada.style.display = 'none';
    });
});
