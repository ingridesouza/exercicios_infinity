async function filterCryptoData(filter) {
    const cryptoData = await getCryptoData();
    const filteredCryptoData = cryptoData.filter(crypto => crypto.name.toLowerCase().startsWith(filter.toLowerCase()));

    const cryptoInfoSection = document.getElementById('crypto-info');
    cryptoInfoSection.innerHTML = '';

    filteredCryptoData.forEach(crypto => {
        const card = document.createElement('div');
        card.classList.add('crypto-card');

        const logo = document.createElement('img');
        logo.src = crypto.logo;
        logo.alt = crypto.name;

        const name = document.createElement('h2');
        name.textContent = crypto.name;

        const price = document.createElement('p');
        price.textContent = `Preço: $${crypto.quote && crypto.quote.USD && crypto.quote.USD.price ? parseFloat(crypto.quote.USD.price).toFixed(2) : 'N/A'}`; 

        const description = document.createElement('p');
        description.textContent = crypto.description || 'Descrição não disponível';
        
        card.appendChild(logo);
        card.appendChild(name);
        card.appendChild(price);
        card.appendChild(description);
        
        cryptoInfoSection.appendChild(card);
    });
}

document.getElementById('filter-input').addEventListener('input', function(event) {
    const filter = event.target.value;
    filterCryptoData(filter);
});

async function getCryptoData() {
    try {
        const response = await fetch('https://api.allorigins.win/raw?url=https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY=1fcac124-9426-42e5-8773-c754f1ebaf1b');
        const data = await response.json();
        return data.data;
    } catch (error) {
        console.error('Erro ao obter dados das criptomoedas:', error);
    }
}




async function fetchCryptoData() {
    try {
        const response = await fetch('https://api.allorigins.win/raw?url=https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Erro ao obter dados das criptomoedas:', error);
    }
}

async function fetchCryptoDataWithSymbols(symbols) {
    try {
        const response = await fetch(`https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=${symbols.join(',')}`);
        const data = await response.json();
        const cryptoData = {};
        data.forEach(crypto => {
            cryptoData[crypto.symbol] = {
                image: crypto.image,
                symbol: crypto.symbol
            };
        });
        return cryptoData;
    } catch (error) {
        console.error('Erro ao obter dados das criptomoedas:', error);
        return {};
    }
}

async function displayCryptoData() {
    const cryptoData = await fetchCryptoData();
    const cryptoSymbols = cryptoData.map(crypto => crypto.symbol);
    const cryptoDataWithSymbols = await fetchCryptoDataWithSymbols(cryptoSymbols);
    const cryptoInfoSection = document.getElementById('crypto-info');

    cryptoData.forEach(crypto => {
        const card = document.createElement('div');
        card.classList.add('crypto-card');

        const logo = document.createElement('img');
        const cryptoInfo = cryptoDataWithSymbols[crypto.symbol];

        if (cryptoInfo && cryptoInfo.image) {
            logo.src = cryptoInfo.image;
        } else {
            logo.src = '';
        }

        logo.alt = crypto.name;

        const name = document.createElement('h2');
        name.textContent = crypto.name;

        const price = document.createElement('p');
        price.textContent = `Preço: $${parseFloat(crypto.current_price).toFixed(2)}`;

        card.appendChild(logo);
        card.appendChild(name);
        card.appendChild(price);

        cryptoInfoSection.appendChild(card);
    });
}

displayCryptoData();




async function convertCurrency(fromCurrencyId, toCurrencySymbol, amount) {
    try {
        const proxyUrl = 'https://cors-anywhere.herokuapp.com/';
        const apiUrl = `https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount=${amount}&symbol=${fromCurrencyId}&convert=${toCurrencySymbol}&CMC_PRO_API_KEY=1fcac124-9426-42e5-8773-c754f1ebaf1b`;
        
        const response = await fetch(proxyUrl + apiUrl);
        const data = await response.json();

        if (data.status.error_code === 0 && data.data && data.data.quote && data.data.quote[toCurrencySymbol]) {
            const convertedAmount = data.data.quote[toCurrencySymbol].price;
            return convertedAmount;
        } else {
            throw new Error("Erro na conversão. Por favor, tente novamente.");
        }
    } catch (error) {
        throw new Error("Erro na conversão. Por favor, tente novamente.");
    }
}




async function populateCurrencySelects() {
    const cryptoData = await getCryptoData();
    const fromCurrencySelect = document.getElementById('from-currency-select');
    const toCurrencySelect = document.getElementById('to-currency-select');

    cryptoData.forEach(crypto => {
        const optionFrom = document.createElement('option');
        optionFrom.value = crypto.symbol.toUpperCase();
        optionFrom.textContent = crypto.symbol.toUpperCase();
        fromCurrencySelect.appendChild(optionFrom);

        const optionTo = document.createElement('option');
        optionTo.value = crypto.symbol.toUpperCase();
        optionTo.textContent = crypto.symbol.toUpperCase();
        toCurrencySelect.appendChild(optionTo);
    });
}

populateCurrencySelects();

async function convertAndDisplay() {
    const amount = parseFloat(document.getElementById('amount-input').value);
    const fromCurrencySymbol = document.getElementById('from-currency-select').value;
    const toCurrencySymbol = document.getElementById('to-currency-select').value;

    try {
        const convertedAmount = await convertCurrency(fromCurrencySymbol, toCurrencySymbol, amount);
        const resultMessage = `O valor da conversão de ${amount} ${fromCurrencySymbol} para ${toCurrencySymbol} é ${convertedAmount.toFixed(2)}`;
        document.getElementById('converted-result').textContent = resultMessage;
    } catch (error) {
        console.error('Erro ao converter moeda:', error);
        const errorMessage = "Erro na conversão. Por favor, tente novamente.";
        document.getElementById('converted-result').textContent = errorMessage;
    }
}

document.getElementById('convert-button').addEventListener('click', convertAndDisplay);

