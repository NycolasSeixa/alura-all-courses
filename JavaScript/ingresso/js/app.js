function comprar() {
    let tipoIngresso = document.getElementById("tipo-ingresso").value;
    let qtd = document.getElementById("qtd").value;
    
    let qtdPista = document.getElementById("qtd-pista");
    let qtdSuperior = document.getElementById("qtd-superior");
    let qtdInferior = document.getElementById("qtd-inferior");

    let nmPista = Number(qtdPista.innerHTML);
    let nmSuperior = Number(qtdSuperior.innerHTML);
    let nmInferior = Number(qtdInferior.innerHTML);

    if (tipoIngresso == "pista"){
        if((nmPista - qtd) >= 0) {
            qtdPista.innerHTML = nmPista - qtd;
        } else {
            alert("Quantidade indisponível!")
        }
    } else if (tipoIngresso == "superior") {
        if((nmSuperior - qtd) >= 0) {
            qtdSuperior.innerHTML = nmSuperior - qtd;
        } else {
            alert("Quantidade indisponível!")
        }
    } else if (tipoIngresso == "inferior") {
        if((nmInferior - qtd) >= 0) {
            qtdInferior.innerHTML = nmInferior - qtd;
        } else {
            alert("Quantidade indisponível!")
        }
    } else {
        alert("Erro no sistema!");
    }

    console.log(tipoIngresso, qtd, qtdPista, qtdSuperior, qtdInferior);

}