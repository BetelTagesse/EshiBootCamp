let hamburger = document.getElementById('nav-hamburger');
let navList = document.getElementById('nav-list');

hamburger.addEventListener('click', () => {
    navList.classList.toggle('nav__list--show');
});