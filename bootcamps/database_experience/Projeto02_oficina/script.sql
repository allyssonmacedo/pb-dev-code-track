CREATE DATABASE oficina;
use oficina;

CREATE TABLE clientes (
idCliente INT PRIMARY KEY,
Nome VARCHAR(45) NOT NULL, 
CPF INT(11) NOT NULL UNIQUE,
Endereço VARCHAR(45)
);

CREATE TABLE serviço (
idServiço INT PRIMARY KEY,
Tipo_serviço ENUM('conserto', 'revisão') NOT NULL,
Descrição VARCHAR(45)
);

CREATE TABLE veiculo (
idVeiculo INT PRIMARY KEY,
Placa VARCHAR(20) NOT NULL,
Modelo VARCHAR(45) NOT NULL,
Ano YEAR NOT NULL,
COR VARCHAR(45) NOT NULL DEFAULT 'branco'
);

CREATE TABLE equipe (




mecanico
ref_Mão_de_obra
Peças



OS_has_serviço
equipe_has_mecanio=co
Serviço_has_peças
