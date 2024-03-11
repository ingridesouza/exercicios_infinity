
async function filterCryptoData(filter) {
    const cryptoData = await getCryptoData();
    const filteredCryptoData = cryptoData.filter(crypto => crypto.name.toLowerCase().includes(filter.toLowerCase()));

    const cryptoInfoSection = document.getElementById('crypto-info');
    cryptoInfoSection.innerHTML = '';

    filteredCryptoData.forEach(crypto => {
        const card = document.createElement('div');
        card.classList.add('crypto-card');

        const logo = document.createElement('img');
        logo.src = crypto.image;
        logo.alt = crypto.name;

        const name = document.createElement('h2');
        name.textContent = crypto.name;

        const price = document.createElement('p');
        price.textContent = `Preço: ${crypto.current_price} USD`;

        const description = document.createElement('p');
        description.textContent = crypto.description;

        card.appendChild(logo);
        card.appendChild(name);
        card.appendChild(price);
        card.appendChild(description);

        card.onclick = function() {
            const content = `
                <h2>${crypto.name}</h2>
                <img src="${crypto.image}" alt="${crypto.name}">
                <p>Preço: ${crypto.current_price} USD</p>
                <p>${crypto.description}</p>
            `;
            showModal(content);
        };

        cryptoInfoSection.appendChild(card);
    });
}

document.getElementById('filter-input').addEventListener('input', function(event) {
    const filter = event.target.value;
    filterCryptoData(filter);
});

const modal = document.getElementById('modal');
const closeBtn = document.getElementsByClassName('close')[0];

function showModal(content) {
    const modalContent = document.getElementById('modal-content');
    modalContent.innerHTML = content;
    modal.style.display = 'block';
}

closeBtn.onclick = function() {
    modal.style.display = 'none';
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}


async function getCryptoData() {
    try {
        const response = await fetch('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Erro ao obter dados das criptomoedas:', error);
    }
}

async function displayCryptoData() {
    const cryptoData = await getCryptoData();
    const cryptoInfoSection = document.getElementById('crypto-info');

    cryptoData.forEach(crypto => {
        const card = document.createElement('div');
        card.classList.add('crypto-card');

        const logo = document.createElement('img');
        logo.src = crypto.image;
        logo.alt = crypto.name;

        const name = document.createElement('h2');
        name.textContent = crypto.name;

        const price = document.createElement('p');
        price.textContent = `Preço: ${crypto.current_price} USD`;

        const description = document.createElement('p');
        description.textContent = crypto.description;

        card.appendChild(logo);
        card.appendChild(name);
        card.appendChild(price);
        card.appendChild(description);

        card.onclick = function() {
            const content = `
                <h2>${crypto.name}</h2>
                <img src="${crypto.image}" alt="${crypto.name}">
                <p>Preço: ${crypto.current_price} USD</p>
                <p>${crypto.description}</p>
            `;
            showModal(content);
        };

        cryptoInfoSection.appendChild(card);
    });
}

displayCryptoData();

async function getCryptoCurrencies() {
    try {
        const response = await fetch('https://api.coingecko.com/api/v3/coins/list');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Erro ao obter lista de criptomoedas:', error);
    }
}

async function populateCurrencySelects() {
    const currencies = await getCryptoCurrencies();
    const fromCurrencySelect = document.getElementById('from-currency-select');
    const toCurrencySelect = document.getElementById('to-currency-select');

    currencies.forEach(currency => {
        const optionFrom = document.createElement('option');
        optionFrom.value = currency.id;
        optionFrom.textContent = currency.name;
        fromCurrencySelect.appendChild(optionFrom);

        const optionTo = document.createElement('option');
        optionTo.value = currency.id;
        optionTo.textContent = currency.name;
        toCurrencySelect.appendChild(optionTo);
    });
}

populateCurrencySelects();

async function convertCurrency() {
    const fromCurrencyId = document.getElementById('from-currency-select').value.toLowerCase();
    const toCurrencySymbol = document.getElementById('to-currency-select').value.toLowerCase();
    const amount = document.getElementById('amount-input').value;

    try {
        const response = await fetch(`https://api.coingecko.com/api/v3/simple/price?ids=${fromCurrencyId}&vs_currencies=${toCurrencySymbol}`);
        const data = await response.json();

        if (data && data[fromCurrencyId] && data[fromCurrencyId][toCurrencySymbol]) {
            const rate = data[fromCurrencyId][toCurrencySymbol];
            const convertedAmount = amount * rate;
            document.getElementById('converted-result').textContent = `${amount} ${fromCurrencyId.toUpperCase()} = ${convertedAmount.toFixed(2)} ${toCurrencySymbol.toUpperCase()}`;
        } else {
            document.getElementById('converted-result').textContent = "Erro na conversão. Por favor, tente novamente.";
        }
    } catch (error) {
        console.error('Erro ao converter moeda:', error);
        document.getElementById('converted-result').textContent = "Erro na conversão. Por favor, tente novamente.";
    }

}


document.getElementById('convert-button').addEventListener('click', convertCurrency);


