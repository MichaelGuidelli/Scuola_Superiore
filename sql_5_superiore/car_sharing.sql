-- Active: 1674252402808@@127.0.0.1@3306
CREATE DATABASE CarSharing;

USE CarSharing;

-- Al nome della relazione ho dovuto aggiungere un underscore perché auto è un comando.
CREATE TABLE Auto_ (
    IdAuto INT AUTO_INCREMENT PRIMARY KEY,
    Targa VARCHAR(7) NOT NULL UNIQUE,
    Modello VARCHAR(255) NOT NULL,
    Colore VARCHAR(255) NOT NULL,
    Alimentazione VARCHAR(255) NOT NULL,
    NumeroTelaio VARCHAR(17) NOT NULL UNIQUE,
    AnnoDiProduzione DATE NOT NULL
);

CREATE TABLE Soci (
    IdSocio INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL,
    Cognome VARCHAR(255) NOT NULL,
    Età INT(3) NOT NULL,
    CodiceFiscale VARCHAR(16) NOT NULL UNIQUE,
    Email VARCHAR(255) NOT NULL UNIQUE,
    Telefono VARCHAR(13) NOT NULL UNIQUE
);

CREATE TABLE AutoSoci (
    IdAuto INT,
    IdSocio INT,
    DataInizio DATE NOT NULL,
    DataFine DATE NOT NULL,
    PRIMARY KEY (IdAuto, IdSocio),
    FOREIGN KEY (IdAuto) REFERENCES Auto_ (IdAuto),
    FOREIGN KEY (IdSocio) REFERENCES Soci (IdSocio)
);

CREATE TABLE Indirizzi (
    IdIndirizzo INT AUTO_INCREMENT PRIMARY KEY,
    Regione VARCHAR(255) NOT NULL,
    Città VARCHAR(255) NOT NULL,
    TipologiaStrada VARCHAR(255) NOT NULL,
    NomeStrada VARCHAR(255) NOT NULL,
    Cap INT(5) NOT NULL,
    Civico INT(255) NOT NULL,
    Palazzina VARCHAR(255),
    Scala VARCHAR(255),
    Piano INT(100)
);

CREATE TABLE SociIndirizzi (
    IdSocio INT,
    IdIndirizzo INT,
    PRIMARY KEY (IdSocio, IdIndirizzo),
    FOREIGN KEY (IdSocio) REFERENCES Soci (IdSocio),
    FOREIGN KEY (IdIndirizzo) REFERENCES Indirizzi (IdIndirizzo)
);
