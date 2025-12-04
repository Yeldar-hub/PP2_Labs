import psycopg2
from config import load_config

def create_phonebook():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            phone VARCHAR(20) UNIQUE NOT NULL
        );
        """,
        """
        CREATE OR REPLACE FUNCTION search_contacts_by_pattern(p_pattern TEXT)
        RETURNS TABLE(id INT, first_name TEXT, phone TEXT)
        AS $$
        BEGIN
            RETURN QUERY
            SELECT * FROM phonebook
            WHERE first_name ILIKE '%' || p_pattern || '%'
               OR phone ILIKE '%' || p_pattern || '%'
            ORDER BY id;
        END;
        $$ LANGUAGE plpgsql;
        """,
        """
        CREATE OR REPLACE FUNCTION upsert_user_by_name(p_name TEXT, p_phone TEXT)
        RETURNS VOID AS $$
        BEGIN
            INSERT INTO phonebook(first_name, phone)
            VALUES (p_name, p_phone)
            ON CONFLICT(phone)
            DO UPDATE SET first_name = EXCLUDED.first_name;
        END;
        $$ LANGUAGE plpgsql;
        """,
        """
        CREATE OR REPLACE FUNCTION insert_many_users(p_names TEXT[], p_phones TEXT[])
        RETURNS TABLE(name TEXT, phone TEXT, error TEXT)
        AS $$
        DECLARE
            i INT;
            phoneRegex TEXT := '^\\+?\\d{5,15}$';
        BEGIN
            FOR i IN 1..array_length(p_names,1) LOOP
                IF NOT(p_phones[i] ~ phoneRegex) THEN
                    name := p_names[i];
                    phone := p_phones[i];
                    error := 'invalid_phone';
                    RETURN NEXT;
                ELSE
                    PERFORM upsert_user_by_name(p_names[i], p_phones[i]);
                END IF;
            END LOOP;
        END;
        $$ LANGUAGE plpgsql;
        """,
        """
        CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
        RETURNS TABLE(id INT, first_name TEXT, phone TEXT)
        AS $$
        BEGIN
            RETURN QUERY
            SELECT * FROM phonebook
            ORDER BY id
            LIMIT p_limit OFFSET p_offset;
        END;
        $$ LANGUAGE plpgsql;
        """,
        """
        CREATE OR REPLACE FUNCTION delete_by_name_or_phone(p_name TEXT, p_phone TEXT)
        RETURNS INT AS $$
        DECLARE
            deleted_rows INT;
        BEGIN
            DELETE FROM phonebook
            WHERE first_name = p_name
               OR phone = p_phone;
            GET DIAGNOSTICS deleted_rows = ROW_COUNT;
            RETURN deleted_rows;
        END;
        $$ LANGUAGE plpgsql;
        """
    )

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
            print("PhoneBook table & functions created successfully!")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    create_phonebook()
