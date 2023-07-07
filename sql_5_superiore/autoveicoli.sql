-- Active: 1674255271051@@127.0.0.1@3306
CREATE DATABASE Motorizzazione;

USE Motorizzazione;

CREATE TABLE Autoveicoli (
    IdAutoveicolo INT AUTO_INCREMENT PRIMARY KEY,
    NumeroTelaio VARCHAR(17) NOT NULL UNIQUE,
    Targa VARCHAR(7) NOT NULL UNIQUE,
    Colore VARCHAR(255) NOT NULL,
    AnnoDiProduzione DATE NOT NULL,
    Alimentazione VARCHAR(255) NOT NULL,
    Modello VARCHAR(255) NOT NULL
);

CREATE TABLE Proprietari (
    IdProprietario INT AUTO_INCREMENT PRIMARY KEY,
    CodiceFiscale VARCHAR(16) NOT NULL UNIQUE,
    Nome VARCHAR(255) NOT NULL,
    Cognome VARCHAR(255) NOT NULL,
    Età INT(3) NOT NULL,
    Nazionalità VARCHAR(255) NOT NULL 
);

CREATE TABLE AutoveicoliProprietari (
    idAutoveicolo INT,
    IdProprietario INT,
    PRIMARY KEY (IdAutoveicolo, IdProprietario),
    FOREIGN KEY (idAutoveicolo) REFERENCES Autoveicoli (IdAutoveicolo),
    FOREIGN KEY (IdProprietario) REFERENCES Proprietari (IdProprietario)
);
