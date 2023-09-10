-- Criando o banco de dados
CREATE DATABASE	ecommerce;
USE ecommerce;

-- Criando a tabela Clientes
CREATE TABLE Clientes (
idCliente INT PRIMARY KEY NOT NULL, 
Tipo ENUM('PJ', 'PF')
);

-- Criando a tabela Vendedor
CREATE TABLE Vendedor (
idVendedor INT NOT NULL PRIMARY KEY, 
Nome VARCHAR(45) NOT NULL,
Loja VARCHAR(45) NOT NULL
);

-- Criando a tabela Produto
CREATE TABLE Produto (
idProduto INT PRIMARY KEY NOT NULL, 
Categoria VARCHAR(45) NOT NULL,
Quantidade INT NOT NULL, 
Preço FLOAT NOT NULL
);

-- Criando a tabela Pagamentos
CREATE TABLE Pagamento (
idPagamento INT PRIMARY KEY NOT NULL,
Método_pagamento ENUM("Cartão", "Boleto", "PIX"),
Data_venc DATE NOT NULL,
Cod_pagamento INT NOT NULL UNIQUE
);

-- Criando a tabela Fornecedor 
CREATE TABLE Fornecedor (
idFornecedor INT PRIMARY KEY NOT NULL,
Razão_social VARCHAR(45) NOT NULL UNIQUE, 
CNPJ CHAR(14) NOT NULL UNIQUE,
Localidade VARCHAR(45),
CEP CHAR(8)
);

-- Criando a tabela de Entrega
CREATE TABLE Entrega (
idEntrega INT NOT NULL PRIMARY KEY,
Data_entrega DATE NOT NULL, 
Data_envio DATE NOT NULL,
Cod_rastreio INT NOT NULL UNIQUE
);

-- Criando tabela Pedidos
CREATE TABLE Pedidos (
idPedido INT PRIMARY KEY AUTO_INCREMENT, 
Status_pedido ENUM('Em andamento', 'cancelado', 'finalizado') DEFAULT 'Em andamento',
Desc_pedido VARCHAR(45) NOT NULL,
Frete FLOAT DEFAULT 0, 
Preço FLOAT, 
Data_pedido DATE NOT NULL,
idCliente INT,
idProduto INT,
idVendedor INT, 
CONSTRAINT fk_idcliente FOREIGN KEY (idCliente) REFERENCES Clientes(idCliente),
CONSTRAINT fk_idproduto FOREIGN KEY (idProduto) REFERENCES Produto(idProduto),
CONSTRAINT fk_idvendedor FOREIGN KEY (idVendedor) REFERENCES Vendedor(idVendedor)
);

-- Criando as tabelas herança de Clientes
CREATE TABLE Cliente_PF (
idCliente INT,
Nome VARCHAR(20) NOT NULL,
Sobrenome VARCHAR(20),
CPF CHAR(11) NOT NULL UNIQUE,
Endereço VARCHAR(45), 
Data_nasc DATE NOT NULL,
CONSTRAINT fk_cliente_pf FOREIGN KEY (idCliente) REFERENCES Clientes(idCliente)
);

CREATE TABLE Cliente_PJ (
idCliente INT,
CNPJ CHAR(14) NOT NULL UNIQUE,
Razão_social VARCHAR(45) NOT NULL,
Endereço VARCHAR(45),
CONSTRAINT fk_cliente_pj FOREIGN KEY (idCliente) REFERENCES Clientes(idCliente)
);

drop table Cliente_PJ;
-- Criando tabelas n:m
CREATE TABLE PedidosPagamentos (
idCliente INT,
CNPJ CHAR(14) NOT NULL UNIQUE,
Razão_social VARCHAR(45) NOT NULL,
Endereço VARCHAR(45),
CONSTRAINT fk_cliente_pj FOREIGN KEY (idCliente) REFERENCES Clientes(idCliente)
);

INSERT INTO Clientes (idCliente, Tipo) values
(1,'PF'),
(2,'PF'),
(3,'PF'),
(4,'PF'),
(5,'PJ'),
(6,'PJ'),
(7,'PJ');

INSERT INTO Cliente_Pf (idCliente, Nome, Sobrenome, CPF, Endereço, Data_nasc) values
(1,'Jonny','MacGillacolm',12345678910,'Mallard',1/28/2018),
(2,'Retha','Wiltshaw',12345678911,'Center',7/2/2012),
(3,'Lenci','Olphert',12345678913,'5128 Oneill Terrace',3/1/2016),
(4,'Xylia','Stain',12345678914,'4224 Heath Drive',11/9/2007);

INSERT INTO Cliente_PJ (idCliente, CNPJ, Razão_social, Endereço) values
(5,12345678910112,'ABC Farm','Center'),
(6,12345678910115,'ABC Milk','South'),
(7,12345678910114,'ABC Eggs','5121 Oha Street');

INSERT INTO Vendedor (idVendedor, Nome, Loja) values
(1,'Mark','Store 1'),
(2,'Blake','Store 2'),
(3,'Sam','Store 1');

INSERT INTO Produto (idProduto, Categoria, Quantidade, Preço) values
(1,'Food', 10, 19.99),
(2,'Food', 13, 12.82),
(3,'Drink', 22, 6.21),
(4,'Chocolate',30, 2.10),
(5,'Drink',0, 10.20),
(6,'Chocolate',50, 1.99);

INSERT INTO Produto (idProduto, Categoria, Quantidade, Preço) values
(1,'Food', 10, 19.99),
(2,'Food', 13, 12.82),
(3,'Drink', 22, 6.21),
(4,'Chocolate',30, 2.10),
(5,'Drink',0, 10.20),
(6,'Chocolate',50, 1.99);

INSERT INTO Pagamento (idPagamento, Método_pagamento, Data_venc, Cod_pagamento) values 
(1,'Cartão', 03/02/2022, 1928),
(2,'Boleto', 03/01/2022, 1912),
(3,'Cartão', 03/07/2022, 1923),
(4,'PIX', 10/02/2022, 2019),
(5,'Cartão', 03/08/2022, 1212),
(6,'Boleto', 03/11/2022, 2421),
(7,'Cartão', 11/02/2022, 1321),
(8,'Cartão', 03/08/2022, 1854);

INSERT INTO Fornecedor (idFornecedor, Razão_social, CNPJ, Localidade, CEP) values
(1, 'ABC Shop', 11345678910123, '21A Centro', 64500000),
(2, 'ABC Store', 11345678910124, '21A Centro', 64500000),
(3, 'ABC Chocolate', 11345678910125, '21A Centro', 64500200),
(4, 'ABC Baby', 11345678910126, '21A Centro', 64500100),
(5, 'ABC Oil', 11345678910127, '21A Centro', 64500900),
(6, 'ABC Cheese', 11345678910128, '21A Centro', 64500000),
(7, 'ABC Clothes', 11345678910129, '21A Centro', NULL);

INSERT INTO Entrega (idEntrega, Data_entrega, Data_envio, Cod_rastreio) values
(1, 08/08/2022, 06/07/2022, 1921),
(2, 10/08/2022, 06/07/2022, 1931),
(3, 11/08/2022, 04/07/2022, 1941),
(4, 12/08/2022, 05/06/2022, 1951),
(5, 12/08/2022, 04/07/2022, 1952),
(6, 10/02/2022, 02/05/2022, 1812),
(7, 12/02/2022, 09/06/2022, 1960),
(8, 08/08/2022, 07/04/2022, 1721);

INSERT INTO Pedidos (idPedido, Status_pedido, Desc_pedido, Frete, Preço, Data_pedido, idCliente, idProduto, idVendedor) values
(1, 'Em andamento', 'Compras', 82.43, 114, 02/02/2022, 3, 2, 1),
(2, 'Em andamento', 'Compras', 21, 114, 02/03/2022, 1, 1, 2),
(3, 'Em andamento', 'Compras', 26, 114, 02/04/2022, 5, 2, 1),
(4, 'finalizado', 'Atacado', 13, 114, 02/05/2022, 5, 4, 2),
(5, 'finalizado', 'Compras', 91, 114, 02/06/2022, 2, 5, 3),
(6, 'Em andamento', 'Compras', 33, 114, 02/06/2022, 1, 1, 2),
(7, 'Em andamento', 'Compras', 65.43, 114, 02/07/2022, 2, 2, 1),
(8, 'cancelado', 'Atacado', 41, 30, 12/01/2022, 1, 2, 2),
(9, 'Em andamento', 'Compras', 22.43, 24, 12/02/2022, 5, 3, 1),
(10, 'finalizado', 'Atacado', 12.43, 32, 12/06/2022, 4, 4, 3),
(11, 'cancelado', 'Compras', 62.4, 14, 11/08/2022, 5, 5, 3),
(12, 'Em andamento', 'Compras', 52.43, 34, 02/09/2022, 3, 1, 2);

select * from Pedidos;

select idPedido, Status_pedido, Frete, Preço, idProduto from Pedidos;

select idPedido, Status_pedido, Frete, Preço, idProduto from Pedidos
where Pedidos.idvendedor = 2;

select idPedido, Status_pedido, Frete, Preço, idProduto from Pedidos
where Pedidos.idvendedor = 2;






