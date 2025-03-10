document.addEventListener("DOMContentLoaded", function() {
    const imgClient = document.getElementById("img-client");

    // Добавляем анимацию при наведении
    imgClient.addEventListener("mouseenter", function() {
        imgClient.style.boxShadow = "0 0 15px rgba(255, 255, 255, 0.5)";
    });

    imgClient.addEventListener("mouseleave", function() {
        imgClient.style.boxShadow = "none";
    });

    // Улучшение пользовательского опыта при фокусе на инпутах
    const inputs = document.querySelectorAll("input");
    inputs.forEach(input => {
        input.addEventListener("focus", () => {
            input.style.background = "rgba(255, 255, 255, 0.3)";
        });
        input.addEventListener("blur", () => {
            input.style.background = "rgba(255, 255, 255, 0.2)";
        });
    });
});
