import psycopg2
import os
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv(dotenv_path=".env", override=True)

print("DB_NAME:", os.getenv("DB_NAME"))
print("DB_USER:", os.getenv("DB_USER"))
print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))
print("DB_HOST:", os.getenv("DB_HOST"))
print("DB_PORT:", os.getenv("DB_PORT"))

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

try:
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor = conn.cursor()
    print("Conexão bem-sucedida!")

    cursor.execute("SELECT * FROM users;")
    rows = cursor.fetchall()
    print("Dados na tabela 'users':", rows)

    cursor.close()
    conn.close()
    print("Conexão fechada.")

except Exception as e:
    print("Erro na conexão:", e)
