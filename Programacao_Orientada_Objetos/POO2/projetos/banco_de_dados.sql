CREATE DATABASE IF NOT EXISTS cadastro;
USE cadastro;

CREATE TABLE IF NOT EXISTS clientes (
    id    INT(11)      AUTO_INCREMENT,
    nome  VARCHAR(30)  NOT NULL,
    email VARCHAR(40)  NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO clientes (nome, email) VALUES
    ('João Silva',      'joao@example.com'),
    ('Maria Oliveira',  'maria@example.com'),
    ('Carlos Souza',    'carlos@example.com');