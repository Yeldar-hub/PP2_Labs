import psycopg2
from config import load_config


def delete_by_name(name):
    modify(name, None)


def delete_by_phone(phone):
    modify(None, phone)


def modify(name, phone):
    try:
        with psycopg2.connect(**load_config()) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT delete_by_name_or_phone(%s,%s)", (name, phone))
                result = cur.fetchone()
                conn.commit()

                if result:
                    print("Rows deleted:", result[0])
                else:
                    print("Ничего не было удалено.")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    print("Выбери действие:")
    print("1 — Удалить по имени")
    print("2 — Удалить по номеру телефона")

    choice = input("Ваш выбор: ")

    if choice == "1":
        name = input("Введите имя: ")
        delete_by_name(name)

    elif choice == "2":
        phone = input("Введите номер: ")
        delete_by_phone(phone)

    