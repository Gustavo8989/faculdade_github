def estoque(codigo:int, preco:float, descricao:str, disponibilidade:bool):
    dicionario = {"id":codigo,
               "Preco":preco,
               "descricao":descricao,
               "disponibilidade":disponibilidade,
               }


estoque(1,200.00,"Ferramenta",True)
