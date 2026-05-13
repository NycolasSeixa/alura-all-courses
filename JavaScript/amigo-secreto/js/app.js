let lista = [];
let listaAmigos = document.getElementById("lista-amigos");
let sorteio = [];
let sorteados = document.getElementById("lista-sorteio");

function adicionar() {
    let inputNomeAmigo = document.getElementById("nome-amigo");
    let nomeAmigo = inputNomeAmigo.value.trim();

    if (nomeAmigo === "") {
        alert("Por favor, digite um nome válido.");
        return; 
    }

    lista.push(nomeAmigo);

    if (listaAmigos.innerHTML == "") {
        listaAmigos.innerHTML = nomeAmigo;
    } else {
        listaAmigos.innerHTML += ", " + nomeAmigo;
    }

    inputNomeAmigo.value = ""; 
    inputNomeAmigo.focus(); 
}

function sortear() {
    sorteio = []; 
    sorteados.innerHTML = "";

    if (lista.length < 2) {
        alert("Adicione pelo menos 2 amigos para fazer o sorteio!");
        return;
    }

    lista.forEach((amigo) => {
        let index = Math.floor(Math.random() * lista.length);
        
        while (lista[index] === amigo || sorteio.includes(index)) {
            index = Math.floor(Math.random() * lista.length);
        }

        sorteio.push(index);
    });

    for (let i = 0; i < lista.length; i++) {
        sorteados.innerHTML += lista[i] + " -> " + lista[sorteio[i]] + "<br>";
    }
}

function reiniciar() {
    sorteio = [];
    lista = [];
    listaAmigos.innerHTML = "";
    sorteados.innerHTML = "";
}