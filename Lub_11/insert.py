import psycopg2
import csv
from config import load_config

def insert_user(first_name, phone):
    try:
        with psycopg2.connect(**load_config()) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT upsert_user_by_name(%s, %s)", (first_name, phone))
                conn.commit()
                print("Inserted/Updated:", first_name, phone)
    except Exception as e:
        print("Error:", e)

def insert_from_csv(csv_path):
    try:
        names = []
        phones = []
        with open(csv_path, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                names.append(row[0])
                phones.append(row[1])

        with psycopg2.connect(**load_config()) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM insert_many_users(%s,%s)", (names, phones))
                errors = cur.fetchall()
                conn.commit()

        if errors:
            print("Invalid phones:", errors)
        else:
            print("CSV uploaded successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    print("Выбери действие:")
    print("1 — Ввести имя и номер вручную")
    print("2 — Загрузить данные из CSV")

    choice = input("Ваш выбор: ")

    if choice == "1":
        name = input("Введите имя: ")
        phone = input("Введите номер телефона: ")
        insert_user(name, phone)

    elif choice == "2":
        path = input("Введите путь к CSV файлу: ")
        insert_from_csv(path)

    else:
        print("Неверный выбор!")
