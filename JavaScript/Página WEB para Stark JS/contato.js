document.getElementById('form_contato').addEventListener('submit', function(event) {
    event.preventDefault();

    var nome = document.getElementById('nome').value;
    var telefone = document.getElementById('telefone').value;
    var email = document.getElementById('email').value;
    var newsletter = document.getElementById('newsletter').checked;
    var mensagem = document.getElementById('mensagem').value;

    
    console.log('Nome:', nome);
    console.log('Telefone:', telefone);
    console.log('E-mail:', email);
    console.log('Newsletter:', newsletter);
    console.log('Mensagem:', mensagem);

    
    document.getElementById('form_contato').reset();
    alert('Sua mensagem foi enviada com sucesso!');
});