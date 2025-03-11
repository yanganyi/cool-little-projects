document.addEventListener('DOMContentLoaded', () => {
    const ths = document.querySelectorAll('th');

    ths.forEach(th => {
        const grip = document.createElement('div');
        grip.classList.add('grip');
        th.appendChild(grip);

        let resizing = false;
        let startX;
        let startWidth;

        grip.addEventListener('mousedown', (e) => {
            resizing = true;
            startX = e.clientX;
            startWidth = th.offsetWidth;
            document.body.classList.add('resizing'); 
            e.preventDefault(); 
        });

        document.addEventListener('mousemove', (e) => {
            if (resizing) {
                const width = startWidth + (e.clientX - startX);
                th.style.width = width + 'px';
            }
        });

        document.addEventListener('mouseup', () => {
            if (resizing) {
                resizing = false;
                document.body.classList.remove('resizing'); 
            }
        });
    });
});