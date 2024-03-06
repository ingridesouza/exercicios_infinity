//array para armazenar os contatos
let contatos = [];

//adicionar um novo contato
function adicionarContato(event) {
    event.preventDefault();

    const nome = document.getElementById('nome').value;
    const telefone = document.getElementById('telefone').value;

    contatos.push({ nome, telefone });
    exibirContatos();
    document.getElementById('form-contato').reset();
}

//exibir a lista de contatos
function exibirContatos() {
    const listaContatos = document.getElementById('lista-contatos');
    listaContatos.innerHTML = '';

    contatos.forEach(contato => {
        const li = document.createElement('li');
        li.innerHTML = `
            <strong>${contato.nome}</strong>: ${contato.telefone}
            <button onclick="editarContato('${contato.nome}')">Editar</button>
            <button class="excluir" onclick="excluirContato('${contato.nome}')">Excluir</button>

        `;
        listaContatos.appendChild(li);
    });
}

//editar um contato
function editarContato(nome) {
    const novoNome = prompt('Digite o novo nome:');
    const novoTelefone = prompt('Digite o novo telefone:');

    const index = contatos.findIndex(contato => contato.nome === nome);
    if (index !== -1) {
        contatos[index] = { nome: novoNome, telefone: novoTelefone };
        exibirContatos();
    }
}

//excluir um contato
function excluirContato(nome) {
    const confirmacao = confirm(`Tem certeza que deseja excluir o contato ${nome}?`);
    if (confirmacao) {
        contatos = contatos.filter(contato => contato.nome !== nome);
        exibirContatos();
    }
}

//evento de submit para o formulário
document.getElementById('form-contato').addEventListener('submit', adicionarContato);

//exibir contatos ao carregar a página
exibirContatos();
