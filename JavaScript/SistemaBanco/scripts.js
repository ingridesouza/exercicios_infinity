let saldo = 1000; // Saldo inicial fictício

        document.getElementById('formulario').addEventListener('submit', function(event) {
            event.preventDefault();
            const operacao = document.getElementById('operacao').value;
            let valor = parseFloat(document.getElementById('valor').value);

            try {
                if (isNaN(valor) || valor <= 0) {
                    throw new Error('Valor inválido.');
                }

                switch (operacao) {
                    case 'consultar':
                        document.getElementById('resultado').innerText = `Seu saldo é de R$ ${saldo.toFixed(2)}.`;
                        break;
                    case 'sacar':
                        if (valor > saldo) {
                            throw new Error('Saldo insuficiente.');
                        }
                        saldo -= valor;
                        document.getElementById('resultado').innerText = `Saque de R$ ${valor.toFixed(2)} realizado. Novo saldo: R$ ${saldo.toFixed(2)}.`;
                        break;
                    case 'depositar':
                        saldo += valor;
                        document.getElementById('resultado').innerText = `Depósito de R$ ${valor.toFixed(2)} realizado. Novo saldo: R$ ${saldo.toFixed(2)}.`;
                        break;
                }
            } catch (error) {
                document.getElementById('resultado').innerText = error.message;
            }
        });