// main.js
class User {
    constructor(username, password) {
        this.username = username;
        this.password = password;
    }
}

class Product {
    constructor(name, description, price, available) {
        this.name = name;
        this.description = description;
        this.price = price;
        this.available = available;
    }
}

// Funções para mostrar/esconder formulários de login e cadastro
function showLoginPage() {
    document.getElementById('loginForm').classList.remove('hidden');
    document.getElementById('registrationForm').classList.add('hidden');
}

function showRegistrationPage() {
    document.getElementById('registrationForm').classList.remove('hidden');
    document.getElementById('loginForm').classList.add('hidden');
}
// main.js (continuação)
let products = [];

// Função para carregar produtos do fakestoreapi
async function loadProducts() {
    const response = await fetch('https://fakestoreapi.com/products');
    const data = await response.json();
    products = data.map(item => new Product(item.title, item.description, item.price, true));
}

// Função para exibir o catálogo de produtos
function displayProducts() {
    const catalog = document.getElementById('catalog');
    catalog.innerHTML = '';

    products.forEach(product => {
        const card = document.createElement('div');
        card.classList.add('productCard');
        card.innerHTML = `
            <h3>${product.name}</h3>
            <p>${product.description}</p>
            <p>Preço: R$ ${product.price.toFixed(2)}</p>
            <button onclick="addToCart('${product.name}')">Adicionar ao Carrinho</button>
        `;
        catalog.appendChild(card);
    });
}
// main.js (continuação)
let cart = [];

// Função para adicionar produto ao carrinho
function addToCart(productName) {
    const product = products.find(item => item.name === productName);
    if (product) {
        cart.push(product);
        updateCartSummary();
    }
}

// Função para atualizar o resumo do carrinho
function updateCartSummary() {
    const cartSummary = document.getElementById('cartSummary');
    cartSummary.innerHTML = '';

    let totalPrice = 0;
    cart.forEach(product => {
        totalPrice += product.price;
        const item = document.createElement('div');
        item.innerHTML = `${product.name} - R$ ${product.price.toFixed(2)}`;
        cartSummary.appendChild(item);
    });

    const total = document.createElement('div');
    total.innerHTML = `<strong>Total: R$ ${totalPrice.toFixed(2)}</strong>`;
    cartSummary.appendChild(total);
}
// main.js (continuação)
function checkout() {
    // Simulação de checkout
    // Aqui você pode adicionar a integração com o AfterShip para enviar a notificação de confirmação de pedido
    alert("Pedido concluído! Notificação de confirmação enviada.");
}
