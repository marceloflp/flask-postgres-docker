## 💾 Projeto Flask + PostgreSQL com Docker

Este projeto é uma aplicação Flask simples que se conecta a um banco de dados PostgreSQL usando containers Docker criados manualmente, sem o uso de Docker Compose.

---

### 📁 Estrutura do Projeto

```
projeto/
├── app.py
├── requirements.txt
├── python.Dockerfile
├── postgres.Dockerfile
└── init.sql
```

---

### 📌 Pré-requisitos

* Docker instalado na máquina.
* Terminal com permissões para executar comandos `docker`.

---

### 🚧 Etapas para Executar o Projeto

---

#### 🔹 1. Construir a imagem do PostgreSQL

```bash
docker build -t meu_postgres -f postgres.Dockerfile .
```

---

#### 🔹 2. Subir o container do PostgreSQL

```bash
docker run -d --name postgresql -e POSTGRES_DB=bd_aplicacao -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=admin -p 5433:5432 meu_postgres
```

> Isso iniciará o banco e criará a tabela `usuarios` automaticamente com os dados iniciais via `init.sql`.

---

#### 🔹 3. Construir a imagem da aplicação Flask

```bash
docker build -t app_flask -f python.Dockerfile .
```

---

#### 🔹 4. Subir o container Flask e conectar ao banco de dados

```bash
docker run -d --name flask_app --link postgresql:postgres -p 5000:5000 app_flask
```

> O parâmetro `--link` permite que o container Flask consiga resolver o nome `postgres` como hostname do banco.

---

### 🧪 Testar a API

Acesse no navegador ou via `curl`:

```
http://localhost:5000/
```

Você verá algo como:

```json
{
  "usuarios": [
    [1, "João"],
    [2, "Maria"],
    [3, "Pedro"]
  ]
}
```

---

### 🔄 Parar e Remover os Containers

```bash
docker stop app_flask postgresql
docker rm app_flask postgresql
```

---

### 🧹 Limpar imagens (opcional)

```bash
docker rmi app_flask postgresql
```

---
