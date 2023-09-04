# CRUD feito em Flask com o banco de dados PostgreSQL

<h1> 📋 Instruções </h1>

1. `git clone https://github.com/AnaCarolinaNeves/Python-Flask.git`
2. No VsCode <img src="https://skillicons.dev/icons?i=vscode" width='30px'/> 
   - Novo terminal:
     - `cd Python-Flask/CRUD`
     - `python3 -m venv .venv`
     - `. .venv/bin/activate`
     - `pip install flask`
     - `pip install psycopg2`
     - `flask run`
3. Criar um novo database no pgAdmin (ou outro gerenciador de bancos de dados do PostgreSQL)
4. Alterar as informações do *app.py* com o nome (DB_NAME), usuario (DB_USER) e senha (DB_PASS) do banco de dados configurado anteriormente
   - Alterações devem ser feitas entre as linhas 8 e 11
5. Para rodar novamente a aplicação com as atualizações:
   - `ctrl + c` no terminal -> para encerrar
   - `flask run` -> rodar novamente
