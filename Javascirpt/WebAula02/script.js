let idade = parseInt(prompt("Informe sua idade")) 
let boby = document.body 
let messagem = document.getElementById("messagem") 

if(idade <= 18){
    boby.style.background = 'Darkred';
    msg.style.fontSize = 'xx-large';
    msg.style.color = 'Cornsilk'; 
    msg.innerHTML = "Você é menor de idade"
}else{
    body.style.background = 'Aquamarine';
    msg.style.fontSize = 'xx-large'
    msg.style.color = 'CadeBlue'
    msg.innerHTML = "Você é maior de idade"
}

