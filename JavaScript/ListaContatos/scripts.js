const formContato = document.getElementById("formContato");
const contatosDiv = document.getElementById("contatos");
let contadorContatos = 1;

formContato.addEventListener("submit", function (event) {
    event.preventDefault();
    adicionarContato();
});

function adicionarContato() {
    const nome = document.getElementById("nome").value;
    const numero = document.getElementById("numero").value;
    const email = document.getElementById("email").value;

    if (nome && numero && email) {
        const contato = {
            id: contadorContatos,
            nome,
            numero,
            email
        };

        exibirContato(contato);
        limparFormulario();
        contadorContatos++;
    }
}

function exibirContato(contato) {
    const divContato = document.createElement("div");
    divContato.classList.add("contato");

    const textoContato = `${contato.id}. ${contato.nome} - ${contato.numero} - ${contato.email}`;

    const pContato = document.createElement("p");
    pContato.textContent = textoContato;

    const btnEditar = document.createElement("button");
    btnEditar.textContent = "Editar";
    btnEditar.addEventListener("click", function () {
        editarContato(contato, divContato);
    });

    const btnExcluir = document.createElement("button");
    btnExcluir.textContent = "Excluir";
    btnExcluir.addEventListener("click", function () {
        excluirContato(divContato);
    });

    divContato.appendChild(pContato);
    divContato.appendChild(btnEditar);
    divContato.appendChild(btnExcluir);

    contatosDiv.appendChild(divContato);
}

function editarContato(contato, divContato) {
    const novoNome = prompt("Novo nome:", contato.nome);
    const novoNumero = prompt("Novo número:", contato.numero);
    const novoEmail = prompt("Novo email:", contato.email);

    if (novoNome !== null && novoNumero !== null && novoEmail !== null) {
        contato.nome = novoNome;
        contato.numero = novoNumero;
        contato.email = novoEmail;

        const textoContato = `${contato.id}. ${contato.nome} - ${contato.numero} - ${contato.email}`;
        divContato.querySelector("p").textContent = textoContato;
    }
}

function excluirContato(divContato) {
    if (confirm("Tem certeza que deseja excluir este contato?")) {
        contatosDiv.removeChild(divContato);
    }
}

function limparFormulario() {
    formContato.reset();
}
