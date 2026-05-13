let monopoly = document.querySelector("#game-1 a");
let ticketToRide = document.querySelector("#game-2 a");
let takenoko = document.querySelector("#game-3 a");

let monopolyImg = document.querySelector("#game-1 div")
let ticketToRideImg = document.querySelector("#game-2 div")
let takenokoImg = document.querySelector("#game-3 div")

function changeName(game, img){
    if(game.innerHTML == "Alugar" ){
        game.innerHTML = "Devolver";
        game.classList.add("dashboard__item__button--return")
        img.classList.add("dashboard__item__img--rented")
    } else {
        game.innerHTML = "Alugar";
        game.classList.remove("dashboard__item__button--return")
        img.classList.remove("dashboard__item__img--rented")
    }
}

function alterarStatus(button){
    if(button == 1){
        changeName(monopoly, monopolyImg);
    }
    else if(button == 2){
        changeName(ticketToRide, ticketToRideImg);
    }
    else{
        changeName(takenoko, takenokoImg);
    }
}