window.onload = () => {
    for (btn of document.querySelectorAll('.btn')) {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            document.body.classList.add('inuse');
            if (e.target.href) {
                location.assign(e.target.href);
            } else {
                e.target.parentElement.submit();
            }
        });
    }
}