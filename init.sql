CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100)
);

INSERT INTO usuarios (nome) VALUES
('João'),
('Maria'),
('Pedro');
