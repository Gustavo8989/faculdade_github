document.getElementById("Enviar").addEventListener("click", function(){
  var email = document.getElementById("email").value 
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  if(regex.test(email)){
    alert("Email valido")
  }else{
    alert("Email invalido")
  }
})
