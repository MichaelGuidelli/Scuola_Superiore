-- Active: 1669769595368@@127.0.0.1@3306
CREATE DATABASE Banca;

USE Banca;

CREATE TABLE Filiali (
    IdFiliale INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL,
    Città VARCHAR(255) NOT NULL,
    Capitale FLOAT NOT NULL
);

CREATE TABLE Prestiti (
    IdPrestito INT AUTO_INCREMENT PRIMARY KEY,
    ImportoPrestito FLOAT NOT NULL, 
    IdUfficio VARCHAR(255) NOT NULL UNIQUE,
    IdImpiegato VARCHAR(255) NOT NULL UNIQUE,
    DataInizio DATE NOT NULL,
    DataFine DATE NOT NULL,
    IdFiliale INT,
    FOREIGN KEY (IdFiliale) REFERENCES Filiali (IdFiliale)
);

CREATE TABLE ContiCorrenti (
    IdContoCorrente INT AUTO_INCREMENT PRIMARY KEY,
    Saldo FLOAT NOT NULL,
    IdFiliale INT,
    FOREIGN KEY (IdFiliale) REFERENCES Filiali (IdFiliale)
);

CREATE TABLE Clienti (
    CodiceFiscale VARCHAR(16) PRIMARY KEY,
    NomeCliente VARCHAR(255) NOT NULL,
    CognomeCliente VARCHAR(255) NOT NULL,
    TipologiaStrada VARCHAR(255) NOT NULL,
    NomeStrada VARCHAR(255) NOT NULL,
    Civico INT NOT NULL,
    Città VARCHAR(255) NOT NULL,
    NumeroTelefonoCliente INT(10) NOT NULL UNIQUE
);

CREATE TABLE ClientiPrestiti (
    CodiceFiscale VARCHAR(16),
    IdPrestito INT, 
    PRIMARY KEY (CodiceFiscale, IdPrestito),
    FOREIGN KEY (CodiceFiscale) REFERENCES Clienti (CodiceFiscale),
    FOREIGN KEY (IdPrestito) REFERENCES Prestiti (IdPrestito)
);

CREATE TABLE ClientiContiCorrenti (
    CodiceFiscale VARCHAR(16),
    IdContoCorrente INT,
    PRIMARY KEY (CodiceFiscale, IdContoCorrente),
    FOREIGN KEY (CodiceFiscale) REFERENCES Clienti (CodiceFiscale),
    FOREIGN KEY (IdContoCorrente) REFERENCES ContiCorrenti (IdContoCorrente)
);
