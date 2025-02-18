# 🍽️ Sistema de Gerenciamento de Reservas

Este projeto é um **sistema de gerenciamento de reservas para restaurantes**, desenvolvido com **Flask e SQLAlchemy**. Ele permite que os usuários façam reservas, editem, excluam e visualizem seus agendamentos em uma interface intuitiva.

### ➕ Funcionalidades

#### Sistema de Cadastro e Login
<ul>Cadastro de usuário: Criação de conta com validação de dados e armazenamento seguro de senhas usando Werkzeug (generate_password_hash).</ul>
<ul>Login e autenticação: Sistema de login seguro, onde as senhas são comparadas de forma segura com o uso de Werkzeug (check_password_hash).</ul>

#### Gerenciamento de reservas
<ul>Criação de novas reservas (nome, data, hora, número de pessoas).</ul>
<ul>Edição de reservas existentes.</ul>
<ul>Exclusão de reservas.</ul>
<ul>Visualização das reservas do usuário.</ul>

## 🚀 Começando

Siga as instruções abaixo para rodar o projeto localmente.

### 📋 Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas:

- [Python](https://www.python.org/) (versão 3.8 ou superior)

### 🛠️ Tecnologias Utilizadas

- [Flask](https://flask.palletsprojects.com/) - Framework web para Python
- [SQLAlchemy](https://www.sqlalchemy.org/) - ORM para manipulação do banco de dados
- [SQLite](https://www.sqlite.org/) - Banco de dados leve e eficiente
- [Werkzeug](https://werkzeug.palletsprojects.com/en/stable/): Biblioteca para hashing e verificação segura de senhas.
- HTML, CSS - Interface do usuário

### 🔧 Instalação

Siga estas etapas para configurar o ambiente:

1. Clone o repositório:

   ```bash
   git clone https://github.com/seuusuario/gerenciamento-reservas.git

2. Acesse o diretório do projeto:

   ```bash
   cd gerenciamento-reservas

3. Crie um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate
   
4. Instale as dependências:

   ```bash
   pip install flask flask-sqlalchemy flask-login
   
5. Execute o script principal:

   ```bash
   cd gerenciamento-reservas

## ✒️ Autores

<li>Desenvolvimento e documentação - <a href='https://github.com/NicolasHaubricht/'>Nicolas Haubricht</a></li> 

##
Feito com dedicação por <a href='https://github.com/NicolasHaubricht/'>Nicolas Haubricht</a>
