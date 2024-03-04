const cadastroBtn = document.querySelector(".criarTarefa");
const containerTarefas = document.querySelector(".tarefas");
cadastroBtn.addEventListener("click", cadastrarTarefa);

let tarefas = []; // Agora a array começa vazia

let contador = 1;

const removerTarefa = (id) => {
    tarefas = tarefas.filter((tarefa) => tarefa.id !== id);
    mostrarTarefa(tarefas);
};

function cadastrarTarefa() {
    const tarefa = document.getElementById("tarefa").value;
    const descricao = document.getElementById("descricao").value;

    if (!tarefa) {
        alert("Preencha a tarefa");
        return;
    }

    const novaTarefa = {
        id: contador,
        completa: false,
        nome: tarefa,
        descricao,
    };

    contador++;

    tarefas.push(novaTarefa);
    mostrarTarefa(tarefas);

    // Limpa os campos após cadastrar a tarefa
    document.getElementById("tarefa").value = "";
    document.getElementById("descricao").value = "";
}

function mostrarTarefa(arrayDeTarefas) {
    containerTarefas.innerHTML = "";

    arrayDeTarefas.forEach((tarefa) => {
        const div = document.createElement("div");
        div.classList.add("tarefa");

        const input = document.createElement("input");
        input.type = "checkbox";
        input.checked = tarefa.completa;
        input.addEventListener("change", () => marcarConcluida(tarefa.id, input.checked));

        const p = document.createElement("p");
        p.textContent = tarefa.nome;
        if (tarefa.completa) {
            p.style.textDecoration = "line-through";
            p.style.color = "green"
        }

        const descricao = document.createElement("p");
        descricao.textContent = tarefa.descricao;

        const buttonRemover = document.createElement("button");
        buttonRemover.textContent = "Apagar";
        buttonRemover.addEventListener("click", () => removerTarefa(tarefa.id));

        div.append(input, p, descricao, buttonRemover);

        containerTarefas.appendChild(div);
    });
}

function marcarConcluida(id, completa) {
    const tarefaIndex = tarefas.findIndex((tarefa) => tarefa.id === id);
    tarefas[tarefaIndex].completa = completa;
    mostrarTarefa(tarefas);
}

// Anotações----------------------------------------------

// const cadastroBtn = document.querySelectorAll("#form-pedido input[type=cheeckbox]")
// const cadastroBtn = document.querySelector(".criarTarefa")
// const containerTarefas = document.querySelector(".tarefas")
// querySelector = pega apenas uma informação
// querySelectorAll = pega mais de um elemento com a msm definição de nome
// cadastroBtn.addEventListener("click", cadastrarTarefa)

// let tarefas = [
//     {id: 1, nome: "Estudar", completa: false, descricao:"HTML, Js, Ts, CSS"},
//     {id: 2, nome: "Lavar a louça", completa: false, descricao: "Para a mãe não bate"},
// ]

// let contador = 3;

// const removerTarefa = (id) => {
//     tarefas = tarefas.filter(tarefa => tarefa.id !== id)

//     mostrarTarefa(tarefas)
// }


// function editarTarefa(){
//         const button = document.createElement('button')
//         button.textContent = "Editar"
//         button.addEventListener('click', cadastrarTarefa(tarefas.id))
// }



// function cadastrarTarefa() { /*função para o cadastro da tarefa*/

//     const tarefa = document.getElementById("tarefa").value
//     const descricao = document.getElementById("descricao").value
    
//     if(!tarefa){
//         alert("Preencha a tarefa")
//         return
//     }

//     const novaTarefa = {
//         id: contador,
//         completa: false,
//         nome: tarefa,
//         descricao
//     }

//     contador++

//     tarefas.push(novaTarefa)
//     mostrarTarefa(Tarefas)
// }

// function mostrarTarefa(arrayDeTarefas){
//     containerTarefas.innerHTML = ""

//     arrayDeTarefas.forEach(tarefa => {
//         const div = document.createElement("div")
//         div.classList.add("tarefa")

//         const input = document.createElement("input")
//         input.type = "checkbox"

//         const p = document.createElement("p")
//         p.textContent = tarefa.nome

//         const descricao = document.createElement("p")
//         descricao.textContent = tarefa.descricao

//         const button = document.createElement('button')
//         button.textContent = "Apagar" 
//         button.addEventListener('click', () => removerTarefa(tarefa.id))

//         div.append(input, p, descricao, button)

//         containerTarefas.appendChild(div)
//     })
// }


    // const div = document.createElement("div") /*criando uma div, container de tarefa*/
    // div.classList.add("tarefa") 

    // const input = document.createElement("input")
    // input.type = "checkbox"
    // // input.addEventListener("input" , (e) => { 
    // //     if(e.target.checked) { /*verificar se está verdadeiro, se está checado*/
    // //         e.target.nextElementsibling.style.color = "gray" /*adicionar a cor*/
    // //         e.target.nextElementsibling.style.textDecoration = "line-through"
    // //     }
    // // })
    
    // const p = document.createElement("P") /*criando P*/
    // p.textContent = tarefa /* o conteudo desse P vai ser tarefa*/

    // const button = document.createElement('button') /*criando botão*/
    // button.textContent = "Remover"
    // button.addEventListener('click', () => removerTarefa(div)) /* adicionando o evento de click e adicionando a função de remover tarefa*/ 
    // /*pega o parametro div e passa pra cá*/
    // /* quando clicarem no botão ele retira todo o conteudo do container*/

    // div.append(input, p, button)

    // containerTarefas.appendChild(div)


