CREATE DATABASE Vivaio;

USE Vivaio;

CREATE TABLE Qualifiche (
    IdQualifica INT AUTO_INCREMENT PRIMARY KEY,
    DescrizioneQualifica TEXT NOT NULL
);

CREATE TABLE Attività (
    IdAttività INT AUTO_INCREMENT PRIMARY KEY,
    DescrizioneAttività TEXT NOT NULL,
    CostoOrario DOUBLE NOT NULL,
    E_I VARCHAR(255 NOT NULL),
    FOREIGN KEY (IdQualifica) REFERENCES Qualifiche (IdQualifica)
);

CREATE TABLE Personale (
    IdDipendente INT AUTO_INCREMENT PRIMARY KEY,
    NomeDipendente VARCHAR(255) NOT NULL,
    CognomeDipendente VARCHAR(255) NOT NULL, 
    DataAssunzione DATE NOT NULL,
    FOREIGN KEY (IdQualifica) REFERENCES Qualifiche (IdQualifica)
);

DROP TABLE PersonalePrestazioni;