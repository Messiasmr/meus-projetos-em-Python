CREATE DATABASE SkyHigh_Airlines;
USE SkyHigh_Airlines;

CREATE TABLE Passageiros (
    CPF_ID INT PRIMARY KEY,
    nome_completo VARCHAR(255),
    telefone VARCHAR(15),
    data_nascimento DATE
);

CREATE TABLE Voos (
    id_voo INT PRIMARY KEY,
    origem VARCHAR(100),
    destino VARCHAR(100),
    data_partida DATETIME,
    data_chegada DATETIME,
    capacidade_total INT
);

CREATE TABLE Reservas_voo (
    id_reserva INT PRIMARY KEY,
    id_passageiro INT,
    id_voo INT,
    data_reserva DATETIME,
    status VARCHAR(20),
    FOREIGN KEY (id_passageiro) REFERENCES Passageiros(CPF_ID),
    FOREIGN KEY (id_voo) REFERENCES Voos(id_voo)
);

CREATE TABLE Pagamentos (
    id_pagamento INT PRIMARY KEY,
    id_reserva INT,
    valor_total DECIMAL(10, 2),
    forma_pagamento VARCHAR(20),
    data_pagamento DATETIME,
    FOREIGN KEY (id_reserva) REFERENCES Reservas_voo(id_reserva)
);
