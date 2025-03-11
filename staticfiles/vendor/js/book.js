document.addEventListener("DOMContentLoaded", function() {
    let container = document.querySelector(".books-container");
    let prevBtn = document.getElementById("prevBtn");
    let nextBtn = document.getElementById("nextBtn");

    let scrollAmount = 0;
    let step = 200;

    prevBtn.addEventListener("click", function() {
        scrollAmount -= step;
        container.style.transform = `translateX(${scrollAmount}px)`;
    });

    nextBtn.addEventListener("click", function() {
        scrollAmount += step;
        container.style.transform = `translateX(${scrollAmount}px)`;
    });
});
