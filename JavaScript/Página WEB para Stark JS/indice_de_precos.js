document.getElementById('updateButton').addEventListener('click', function() {
    var selectedCurrency = document.getElementById('currencySelect').value;
    var tableRows = document.querySelectorAll('#cryptoTable tbody tr');
    
    tableRows.forEach(function(row) {
        var priceCell = row.querySelector('td:nth-child(2)');
        var priceAttr = 'data-price-' + selectedCurrency;
        var price = priceCell.getAttribute(priceAttr);
        
        priceCell.textContent = selectedCurrency.toUpperCase() + ' ' + price;
    });
});