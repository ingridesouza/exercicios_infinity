document.addEventListener("DOMContentLoaded", function() {
    const dropdowns = document.querySelectorAll(".dropdown"); 

    dropdowns.forEach(function(dropdown) {
        const dropdownToggle = dropdown.querySelector(".nav-link"); 
        const dropdownMenu = dropdown.querySelector(".dropdown-menu"); 

        dropdownToggle.addEventListener("click", function(event) {
            event.preventDefault(); 
            dropdownMenu.style.display = (dropdownMenu.style.display === "block") ? "none" : "block"; 
        });

        
        dropdown.addEventListener("mouseleave", function() {
            dropdownMenu.style.display = "none";
        });
    });
});



// ---------------------- REDIRECIONAMENTO -------------------------
document.getElementById("search-form").addEventListener("submit", function(event) {
    event.preventDefault();
    redirectToCriptopedia();
});

function redirectToCriptopedia() {
    var searchTerm = document.getElementById("search").value.toLowerCase();
    switch (searchTerm) {
        case "bitcoin":
            window.location.href = "./bitcoin.html";
            break;
        case "ethereum":
            window.location.href = "./ethereum.html";
            break;
        case "solana":
            window.location.href = "./solana.html";
            break;
        case "cardano":
            window.location.href = "./cardano.html";
            break;
        case "ripple":
            window.location.href = "./ripple.html";
            break;
        case "dogecoin":
            window.location.href = "./Dogecoin.html";
            break;
        case "polkadot":
            window.location.href = "./polkadot.html";
            break;
        case "polygon":
            window.location.href = "./Polygon.html";
            break;
        case "kadena":
            window.location.href = "./kadena.html";
            break;
        case "cosmos":
            window.location.href = "./cosmos.html";
            break;
        default:
            alert("Criptomoeda não encontrada na Criptopédia!");
            break;
    }
}