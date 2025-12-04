import psycopg2
from config import load_config

def get_all_contacts():
    try:
        with psycopg2.connect(**load_config()) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM get_contacts_paginated(10000,0)")
                rows = cur.fetchall()
                if rows:
                    for row in rows:
                        print(row)
                else:
                    print("Нет контактов.")
    except Exception as e:
        print("Error:", e)


def find_by_name(name):
    try:
        with psycopg2.connect(**load_config()) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM search_contacts_by_pattern(%s)", (name,))
                rows = cur.fetchall()
                if rows:
                    for row in rows:
                        print(row)
                else:
                    print("Ничего не найдено.")
    except Exception as e:
        print("Error:", e)


def find_by_phone(phone):
    find_by_name(phone)

if __name__ == "__main__":
    print("Выбери действие:")
    print("1 — Показать ВСЕ контакты")
    print("2 — Найти по имени")
    print("3 — Найти по номеру телефона")

    choice = input("Ваш выбор: ")

    if choice == "1":
        get_all_contacts()

    elif choice == "2":
        n = input("Введите имя или часть имени: ")
        find_by_name(n)

    elif choice == "3":
        p = input("Введите номер или часть номера: ")
        find_by_phone(p)

    else:
        print("Неверный выбор!")
