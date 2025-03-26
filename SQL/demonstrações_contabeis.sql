CREATE TABLE demonstracoes_contabeis (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cnpj_operadora VARCHAR(20) NOT NULL,
    ano INT NOT NULL,
    trimestre INT,
    receita DECIMAL(15, 2),
    despesa DECIMAL(15, 2),
    evento_categoria VARCHAR(255),
    valor DECIMAL(15, 2)
);
