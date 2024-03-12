function formatNumber(number) {
    return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function calculate() {
    var cryptoAmount = parseFloat(document.getElementById("cryptoAmount").value);
    var cryptoCurrency = document.getElementById("cryptoSelect").value;
    var currency = document.getElementById("currencySelect").value;
    
    var price;
    switch (cryptoCurrency) {
        case "bitcoin":
            price = {
                usd: 66945,
                eur: 61102,
                gbp: 46797,
                jpy: 9893600,
                rur: 3900027,
                krw: 88596360,
                try: 2171554,
                brl: 333655,
                cny: 481906
            };
            break;
        case "ethereum":
            price = {
                usd: 3886,
                eur: 3546,
                gbp: 2678,
                jpy: 571253,
                rur: 316215,
                krw: 5132089,
                try: 125820,
                brl: 19335,
                cny: 27915
            };
            break;
        case "solana":
            price = {
                usd: 145.50,
                eur: 132.80,
                gbp: 105.07,
                jpy: 21514.93,
                rur: 11830.91,
                krw: 192416.27,
                try: 4720.00,
                brl: 725,
                cny: 1046.62
            };
            break;
        case "cardano":
            price = {
                usd: 0.74,
                eur: 0.67,
                gbp: 0.55,
                jpy: 110.31,
                rur: 63.54,
                krw: 986.58,
                try: 24.16,
                brl: 3.71,
                cny: 5.36
            };
            break;
        case "ripple":
            price = {
                usd: 0.62,
                eur: 0.57,
                gbp: 0.50,
                jpy: 93.52,
                rur: 54.31,
                krw: 832.69,
                try: 20.40,
                brl: 3,
                cny: 4.53
            };
            break;
        case "dogecoin":
            price = {
                usd: 0.15,
                eur: 0.14,
                gbp: 0.10,
                jpy: 23.20,
                rur: 11.71,
                krw: 207.55,
                try: 5.08,
                brl: 1,
                cny: 1.12
            };
            break;
        case "polkadot":
            price = {
                usd: 10.55,
                eur: 9.65,
                gbp: 8.24,
                jpy: 1541.90,
                rur: 799.28,
                krw: 13922.16,
                try: 341.50,
                brl: 53,
                cny: 75.73
            };
            break;
        case "polygon":
            price = {
                usd: 1.16,
                eur: 1.06,
                gbp: 0.87,
                jpy: 172.13,
                rur: 95.97,
                krw: 1539.42,
                try: 37.85,
                brl: 6,
                cny: 8.41
            };
            break;
        case "kadena":
            price = {
                usd: NaN,
                eur: NaN,
                gbp: NaN,
                jpy: NaN,
                rur: NaN,
                krw: NaN,
                try: NaN,
                brl: NaN,
                cny: NaN
            };
            break;
        case "cosmos":
            price = {
                usd: 13.88,
                eur: 12.65,
                gbp: 10.80,
                jpy: 2051.66,
                rur: 1259.85,
                krw: 18348.82,
                try: 450.20,
                brl: 59.51,
                cny: 99.81
            };
            break;
    }

    var convertedPrice = price[currency] * cryptoAmount;
    document.getElementById("result").textContent = formatNumber(convertedPrice.toFixed(2)) + " " + currency.toUpperCase();
}