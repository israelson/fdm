#!/bin/bash

# Defina as variáveis de conexão com o MySQL
DB_USER="root"
DB_PASSWORD="sua_senha"
DB_NAME="avatar_rpg_db"

# Conecte-se ao MySQL e execute os comandos SQL
mysql -u $DB_USER -p$DB_PASSWORD <<EOF

-- Cria o banco de dados se ele não existir
CREATE DATABASE IF NOT EXISTS $DB_NAME;

-- Usa o banco de dados criado
USE $DB_NAME;

-- Cria a tabela sheets
CREATE TABLE IF NOT EXISTS sheets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    character_name VARCHAR(100),
    manual VARCHAR(50),
    attributes JSON,
    movements JSON,
    story TEXT,
    inventory JSON,
    relations JSON,
    fighting_style VARCHAR(50),
    demeanor VARCHAR(50),
    connections JSON
);

-- Cria a tabela conditions
CREATE TABLE IF NOT EXISTS conditions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sheet_id INT,
    afraid TINYINT(1) DEFAULT 0,
    angry TINYINT(1) DEFAULT 0,
    guilty TINYINT(1) DEFAULT 0,
    insecure TINYINT(1) DEFAULT 0,
    troubled TINYINT(1) DEFAULT 0,
    FOREIGN KEY (sheet_id) REFERENCES sheets(id) ON DELETE CASCADE
);

-- Cria a tabela users
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);

EOF

echo "Banco de dados e tabelas criados com sucesso!"
