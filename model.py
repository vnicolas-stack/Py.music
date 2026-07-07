import os
import subprocess
import psycopg2
import psycopg2.extras
from psycopg2 import sql

HOST = "localhost"
PORT = "5432"
DB_NAME = "biblioteca"
USER = "postgres"
PASSWORD = "postgres"

# Cria o banco se não existir
def criar_banco():
    conn = psycopg2.connect(
        host=HOST,
        port=PORT,
        dbname="postgres",
        user=USER,
        password=PASSWORD
    )

    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(
        "SELECT 1 FROM pg_database WHERE datname = %s",
        (DB_NAME,)
    )

    if cur.fetchone() is None:
        cur.execute(
            sql.SQL("CREATE DATABASE {}").format(
                sql.Identifier(DB_NAME)
            )
        )
        print("Banco criado com sucesso!")
    else:
        print("Banco já existe.")

    cur.close()
    conn.close()


# Conexão com o banco
def get_conn():
    return psycopg2.connect(
        host=HOST,
        port=PORT,
        dbname=DB_NAME,
        user=USER,
        password=PASSWORD
    )

# Opção 1: Criar tabela e dados pelo python
def criar_tabela():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id SERIAL PRIMARY KEY,
            titulo VARCHAR(100) NOT NULL
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS musica (
            id SERIAL PRIMARY KEY,
            titulo VARCHAR(300) NOT NULL,
            artista VARCHAR(200) NOT NULL
            streams INTEGER,
            id_categoria INT NULL,
            FOREIGN KEY (id_categoria) REFERENCES categorias(id)
        );
    """)


    cur.execute("SELECT COUNT(*) FROM musica")

    if cur.fetchone()[0] == 0:
        cur.executemany(
            "INSERT INTO musica (titulo, artista, streams, id_categoria) VALUES (%s, %s)",
                [
                    ("The Blonde", "TV Girl", 198000000, ""),
                    ("Sweater Weather", "The Neighbourhood", 2765000000, "" )
                ]
        )

    conn.commit()
    cur.close()
    conn.close()

    print("Tabela criada e dados iniciais inseridos.")