import psycopg2
from psycopg2 import OperationalError

# Настройки подключения
config = {
    "host": "localhost",
    "port": 5435,            # ← обязательно 5435
    "database": "postgres",  
    "user": "postgres",      
    "password": "ashidarx7"  # ← вставь свой пароль
}

def connect_to_postgres(cfg):
    try:
        with psycopg2.connect(**cfg) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT version();")
                version = cur.fetchone()
                print("Connected to PostgreSQL server!")
                print("PostgreSQL version:", version[0])
    except OperationalError as e:
        print("Ошибка подключения:", e)
    except Exception as e:
        print("Произошла ошибка:", e)

if __name__ == "__main__":
    connect_to_postgres(config)