const buttonsContainer = document.getElementById('buttons-container');
const imagesContainer = document.getElementById('images-container');

// Obtendo raças de cachorros da API
fetch('https://dog.ceo/api/breeds/list/all')
    .then(response => response.json())
    .then(data => {
        const breeds = Object.keys(data.message);

        breeds.forEach(breed => {
            const button = document.createElement('button');
            button.textContent = breed;
            button.className = 'button';
            button.addEventListener('click', () => fetchImages(breed));
            buttonsContainer.appendChild(button);
        });
    })
    .catch(error => console.error('Erro ao obter raças de cachorros:', error));

// Função para obter e exibir imagens de uma raça específica
function fetchImages(breed) {
    imagesContainer.innerHTML = '';

    fetch(`https://dog.ceo/api/breed/${breed}/images/random/4`)
        .then(response => response.json())
        .then(data => {
            data.message.forEach(imageUrl => {
                const image = document.createElement('img');
                image.src = imageUrl;
                image.className = 'image';
                imagesContainer.appendChild(image);
            });
        })
        .catch(error => console.error(`Erro ao obter imagens da raça ${breed}:`, error));
}