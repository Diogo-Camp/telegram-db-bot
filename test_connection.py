import psycopg2
import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

# Pegar credenciais do .env
DATABASE = os.getenv("DB_NAME")
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")

try:
    # Conectar ao PostgreSQL
    conn = psycopg2.connect(
        dbname=DATABASE,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )
    
    # Criar um cursor
    cursor = conn.cursor()
    
    # Testar conexão
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"Conectado ao PostgreSQL: {db_version[0]}")

    # Fechar conexão
    cursor.close()
    conn.close()

except Exception as e:
    print(f"Erro ao conectar ao PostgreSQL: {e}")
