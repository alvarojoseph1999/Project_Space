window.addEventListener('scroll', function() {
    const scrollPosition = window.scrollY;
    const container = document.querySelector('.container');

    if (scrollPosition > 100) { // Ajusta la posición de scroll donde quieres activar la animación
        container.classList.add('scroll-active');
    } else {
        container.classList.remove('scroll-active');
    }
});



