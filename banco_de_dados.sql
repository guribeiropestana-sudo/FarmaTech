CREATE DATABASE farmatech;
USE farmatech;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(50) NOT NULL UNIQUE,
    senha VARCHAR(50) NOT NULL,
    tipo ENUM('admin', 'comprador') NOT NULL
);

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    preco DECIMAL(10,2),
    quantidade INT
);

CREATE TABLE vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    total DECIMAL(10,2),
    forma_pagamento VARCHAR(50),
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO usuarios (login, senha, tipo)
VALUES
('admin', '123', 'admin'),
('gustavo', '456', 'comprador');

INSERT INTO produtos (nome, preco, quantidade) VALUES
('Dipirona', 5.50, 100),
('Paracetamol', 7.90, 80),
('Ibuprofeno', 12.00, 50),
('Amoxicilina', 25.00, 30);
