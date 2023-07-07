-- Active: 1669769595368@@127.0.0.1@3306
CREATE DATABASE Concerto;

USE Concerto;

CREATE TABLE Sale (
    IdSala INT AUTO_INCREMENT PRIMARY KEY,
    NomeSala VARCHAR(255) NOT NULL UNIQUE, 
    CapienzaSala INT NOT NULL
);

CREATE TABLE Gruppi (
    NomeGruppo VARCHAR(255) PRIMARY KEY
);

CREATE TABLE Concerti (
    IdConcerto INT AUTO_INCREMENT PRIMARY KEY,
    TitoloConcerto VARCHAR(255) NOT NULL, 
    DataConcerto DATE NOT NULL, 
    DescrizioneConcerto TEXT NOT NULL, 
    IdSala INT,
    NomeGruppo VARCHAR(255), 
    FOREIGN KEY (IdSala) REFERENCES Sale (IdSala),
    FOREIGN KEY (NomeGruppo) REFERENCES Gruppi (NomeGruppo)
);

CREATE TABLE Brani (
    IdBrano INT AUTO_INCREMENT PRIMARY KEY,
    TitoloBrano VARCHAR(255) NOT NULL, 
    AutoreBrano VARCHAR(255) NOT NULL,
    IdConcerto INT, 
    FOREIGN KEY (IdConcerto) REFERENCES Concerti (IdConcerto)
);

CREATE TABLE Musicisti (
    MatricolaMusicista INT AUTO_INCREMENT PRIMARY KEY,
    NomeMusicista VARCHAR(255) NOT NULL,
    CognomeMusicista VARCHAR(255) NOT NULL
);

CREATE TABLE GruppiMusicisti (
    NomeGruppo VARCHAR(255),
    MatricolaMusicista INT,
    PRIMARY KEY (NomeGruppo, MatricolaMusicista)
    FOREIGN KEY (NomeGruppo) REFERENCES Gruppi (NomeGruppo),
    FOREIGN KEY (MatricolaMusicista) REFERENCES Musicisti (MatricolaMusicista)
);

CREATE TABLE Strumenti (
    NomeStrumento VARCHAR(255) PRIMARY KEY
);

CREATE TABLE MucisistiStrumenti (
    MatricolaMusicista INT,
    NomeStrumento VARCHAR(255),
    PRIMARY KEY (MatricolaMusicista, NomeStrumento),
    FOREIGN KEY (MatricolaMusicista) REFERENCES Musicisti ( MatricolaMusicista),
    FOREIGN KEY (NomeStrumento) REFERENCES Strumenti (NomeStrumento)
);