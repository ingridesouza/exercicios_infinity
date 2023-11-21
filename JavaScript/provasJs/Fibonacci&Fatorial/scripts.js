function calcular() {
    //variavel numero criada para guardar o valor do input que foi puxado atraves do id usando o document,getElementById
    let numero = parseInt(document.getElementById("numberInput").value);

    //verificar se o número é válido, caso não seja um número inteiro e positivo, irá aparecer a mensagem
    if (isNaN(numero) || numero < 0) {
        alert("Digite um número inteiro positivo válido.");
        return;
    }

    //calcula o fatorial
    let fatorial = calcularFatorial(numero);

    //calcula a sequência de Fibonacci
    let fibonacciSequencia = calcularFibonacci(numero);

    //exibe os resultados selecionando o id do p html, criando um texto em html para mostrar o resultado
    document.getElementById("resFatorial").innerText = "Fatorial de " + numero + ": " + fatorial;
    
    document.getElementById("resFibonacci").innerText = "Sequência de Fibonacci até " + numero + ": " + fibonacciSequencia.join(", ");

    //mostra os resultados pegando o id da div q estava escondida
    document.getElementById("results").classList.remove("hidden");
}

//função para o calculo do Fatorial
function calcularFatorial(numero) {
    if (numero === 0 || numero === 1) {
        return 1;
    } else {
        return numero * calcularFatorial(numero - 1);
    }
}

//função para calcular a sequencia Fibonacci
function calcularFibonacci(numero) {
    let fibonacciArray = [];
    for (let i = 0; i <= numero; i++) {
        if (i <= 1) {
            fibonacciArray.push(i);
        } else {
            fibonacciArray.push(fibonacciArray[i - 1] + fibonacciArray[i - 2]);
        }
    }
    return fibonacciArray;
}
