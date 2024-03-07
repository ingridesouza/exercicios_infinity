const buttonsContainer = document.getElementById('buttons-container');
const imagesContainer = document.getElementById('images-container');


async function fetchDogBreeds() {
    try {
        const response = await fetch('https://dog.ceo/api/breeds/list/all');
        if (!response.ok) {
            throw new Error('Falha ao obter raças de cachorros');
        }
        const data = await response.json();
        return Object.keys(data.message);
    } catch (error) {
        throw new Error('Erro ao buscar raças de cachorros. Por favor, tente novamente mais tarde.');
    }
}

async function fetchImages(breed) {
    try {
        const response = await fetch(`https://dog.ceo/api/breed/${breed}/images/random/4`);
        if (!response.ok) {
            throw new Error(`Falha ao obter imagens para a raça ${breed}`);
        }
        const data = await response.json();
        return data.message;
    } catch (error) {
        throw new Error(`Erro ao buscar imagens para a raça ${breed}. Por favor, tente novamente mais tarde.`);
    }
}

async function displayDogGallery() {
    try {
        console.log('Carregando...');

        const breeds = await fetchDogBreeds();
        if (!breeds) {
            throw new Error('Falha ao obter raças de cachorros. Não é possível exibir a galeria.');
        }

        breeds.forEach(breed => {
            const button = document.createElement('button');
            button.textContent = breed;
            button.className = 'button';
            button.addEventListener('click', async () => {
                try {
                    imagesContainer.innerHTML = ''; 

                    const breedImages = await fetchImages(breed);
                    if (!breedImages) {
                        throw new Error('Falha ao obter imagens para a raça. Não é possível exibir imagens.');
                    }

                    breedImages.forEach(imageUrl => {
                        const image = document.createElement('img');
                        image.src = imageUrl;
                        image.className = 'image';
                        imagesContainer.appendChild(image);
                    });
                } catch (error) {
                    console.error(error.message);
                }
            });
            buttonsContainer.appendChild(button);
        });
    } catch (error) {
        console.error(error.message);
    }
}

displayDogGallery();
