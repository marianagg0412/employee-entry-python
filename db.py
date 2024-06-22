import psycopg2
from config import Config

def get_db_connection():
    conn = psycopg2.connect(
        host=Config.DATABASE_HOST,
        database=Config.DATABASE_NAME,
        user=Config.DATABASE_USER,
        password=Config.DATABASE_PASSWORD
    )
    return conn
