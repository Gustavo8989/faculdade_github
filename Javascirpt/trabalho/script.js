document.getElementById("Enviar").addEventListener("click", function(){
    var email = document.getElementById("email").value
    var senha = document.getElementById("senha").value 
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/   
    const verificar_senha = /[A-Za-z0-9_-]/
    if(regex.test(email)){
        alert("Email valido")
    }else{
        alert("Email invalido")
    }
})
