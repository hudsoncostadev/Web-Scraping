CREATE TABLE operadoras (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cnpj VARCHAR(20) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    tipo_plano VARCHAR(100),
    situacao VARCHAR(100),
    municipio VARCHAR(100),
    uf VARCHAR(2)
);
