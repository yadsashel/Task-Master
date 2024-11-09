// control the visibility of the navbar menu on mobile
document.addEventListener("DOMContentLoaded", function() {
    const hamburger = document.querySelector(".hamburger");
    const navbarList = document.querySelector(".navbar__list");

    hamburger.addEventListener("click", function() {
        navbarList.classList.toggle("active");
    });
});