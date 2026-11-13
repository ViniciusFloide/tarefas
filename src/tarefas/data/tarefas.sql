CREATE DATABASE IF NOT EXISTS seu_banco;
USE seu_banco;
 
CREATE TABLE IF NOT EXISTS tarefa (
    id_tarefa INT AUTO_INCREMENT PRIMARY KEY,
    titulo_tarefa VARCHAR(150) NOT NULL,
    data_conclusao DATETIME DEFAULT NULL
);
 