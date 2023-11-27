const url = "https://jsonplaceholder.typicode.com/posts";

const loadingElement = document.querySelectorAll("#loading");
const postsContainer = document.querySelector ("#posts-container");

async function getAllPosts(){

    const response = await fetch(url);
    console.log(response);

    //recebe os dados da resposta em formato de array de objetos
    const data = await response.json();
    console.log(data);

    //escondendo a div loading acessando o class list dele e adicionando o hide, a classe de esconder
    loadingElement.classList.add("hide");

    //usando o map para passar por todos os elementos q vieram na requisição chamando eles de post, dps criou elementos html para inserir cada post
    data.map((post) => {
        const div = document.createElement("div")
        const title = document.createElement("h2")
        const body = document.createElement("p")
        const link = document.createElement("a")

        //preenchendo os elementos com conteúdof
        title.innerText = post.title;
        body.innerText = post.body;
        link.innerText = "Ler"
        link.setAttribute("href", `/post.html?id=${post.id}`);

        //div que vai receber todos os elementos de cada post
        div.appendChild(title);
        div.appendChild(body);
        div.appendChild(link);

        postsContainer.appendChild(div);
    })
}

//executa a função
getAllPosts();