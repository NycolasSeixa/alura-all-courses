const listaProdutos = document.getElementById("lista-produtos");
const valorTotal = document.getElementById("valor-total");

let total = 0;

function precoTotal() {
    let produtos = document.querySelectorAll("#lista-produtos .carrinho__produtos__produto");

    total = 0;

    produtos.forEach((produto) => {
        let quantidade = parseInt(produto.querySelector(".texto-azul").textContent);
        let precoTexto = produto.querySelectorAll(".texto-azul")[1].textContent;
        let preco = parseFloat(precoTexto.replace("R$", "").trim());

        total += (quantidade * preco);
    });

    valorTotal.innerHTML = `R$${total.toFixed(2)}`;
}

function adicionar() {
    let quantidade = Number(document.getElementById("quantidade").value);
    let produto = document.getElementById("produto").value.split(" - ");
    let preco = valor(produto[0]);

    if (quantidade > 0) {
        listaProdutos.innerHTML += `
            <section class="carrinho__produtos__produto">
                <span class="texto-azul"> ${quantidade}x </span> ${produto[0]} <span class="texto-azul"> R$${preco} </span>
            </section>
        `;

        precoTotal();
    }
}

function limpar() {
    listaProdutos.innerHTML = '';
    total = 0;
    valorTotal.innerHTML = `R$${total.toFixed(2)}`;
}

function valor(produto) {
    if (produto == "Fone de ouvido") {
        return 100;
    } else if (produto == "Celular") {
        return 1400;
    } else if (produto == "Oculos VR") {
        return 5000;
    }
    return 0;
}
