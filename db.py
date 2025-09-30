import psycopg2 as pg 
from dotenv import load_dotenv
import os

load_dotenv()

params = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
}

def conectar():
    try:
        conexao = pg.connect(**params)
        cursor = conexao.cursor()
        return conexao, cursor
    except Exception as erro:
        print(f"Erro de conexão: {erro}")
        return None, None
    
conexao, cursor = conectar()
cursor.execute(
    "INSERT INTO alunos (nome, idade) VALUES (%s,%s)",
    ("Iago", 18)
)
conexao.commit()
conexao.close()   



