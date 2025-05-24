-- Adicionando a chave estrangeira Clientes_ID na tabela ContaReceber
ALTER TABLE ContaReceber
ADD CONSTRAINT fk_cliente_contareceber
FOREIGN KEY (Clientes_ID)
REFERENCES Cliente(ID);

-- Adicionando a chave estrangeira Municipio_ID na tabela Cliente
ALTER TABLE Cliente
ADD CONSTRAINT fk_municipio_cliente
FOREIGN KEY (Municipio_ID)
REFERENCES Municipio(ID);

-- Adicionando a chave estrangeira Estado_id na tabela Municipio
ALTER TABLE Municipio
ADD CONSTRAINT fk_estado_municipio
FOREIGN KEY (Estado_id)
REFERENCES Estado(ID);