let livros = [];

function carregarLivros() {
    const livrosSalvos = localStorage.getItem('livros');
    if (livrosSalvos) {
        livros = JSON.parse(livrosSalvos);
        exibirLivros();
    }
}

function salvarLivros() {
    localStorage.setItem('livros', JSON.stringify(livros));
}

function exibirLivros() {
    const containerLivros = document.getElementById('livros');
    containerLivros.innerHTML = '';

    livros.forEach((livro, index) => {
        const livroHTML = `
            <div class="livro" style="animation-delay: ${index * 0.1}s;">
                <h2>${livro.titulo}</h2>
                <p>Autor: ${livro.autor}</p>
                <p>Gênero: ${livro.genero}</p>
                <p>Ano de Publicação: ${livro.ano_publicacao}</p>
                <p>Avaliação: ${livro.avaliacao}</p>
            </div>
        `;
        containerLivros.innerHTML += livroHTML;
    });
}

function buscarLivro() {
    const termoBusca = document.getElementById('busca').value.toLowerCase();

    const livrosFiltrados = livros.filter(livro => {
        return livro.titulo.toLowerCase().includes(termoBusca) ||
               livro.autor.toLowerCase().includes(termoBusca) ||
               livro.genero.toLowerCase().includes(termoBusca);
    });

    exibirLivrosFiltrados(livrosFiltrados);
}

function exibirLivrosFiltrados(livrosFiltrados) {
    const containerLivros = document.getElementById('livros');
    containerLivros.innerHTML = '';

    livrosFiltrados.forEach((livro, index) => {
        const livroHTML = `
            <div class="livro" style="animation-delay: ${index * 0.1}s;">
                <h2>${livro.titulo}</h2>
                <p>Autor: ${livro.autor}</p>
                <p>Gênero: ${livro.genero}</p>
                <p>Ano de Publicação: ${livro.ano_publicacao}</p>
                <p>Avaliação: ${livro.avaliacao}</p>
            </div>
        `;
        containerLivros.innerHTML += livroHTML;
    });
}

function adicionarLivro(event) {
    event.preventDefault();

    const titulo = document.getElementById('titulo').value;
    const autor = document.getElementById('autor').value;
    const genero = document.getElementById('genero').value;
    const ano = document.getElementById('ano').value;
    const avaliacao = document.getElementById('avaliacao').value;

    if (!titulo || !autor || !genero || !ano || !avaliacao) {
        alert('Por favor, preencha todos os campos.');
        return;
    }

    livros.push({
        titulo: titulo,
        autor: autor,
        genero: genero,
        ano_publicacao: parseInt(ano),
        avaliacao: parseFloat(avaliacao)
    });

    salvarLivros();
    exibirLivros();
    document.getElementById('formulario').reset();
}

carregarLivros();

document.getElementById('formulario').addEventListener('submit', adicionarLivro);
