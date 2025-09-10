import sqlite3

db_file = "my_inventory.db"

try:
    conn = sqlite3.connect(db_file)
    print(f"Connection to database '{db_file}' successfully established.")

    cursor = conn.cursor()

    create_table_user = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        steam_id TEXT NOT NULL UNIQUE,
        nome_perfil TEXT,
        email TEXT,
        password TEXT
    );
    """

    create_table_skins = """
    CREATE TABLE IF NOT EXISTS skins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT NOT NULL,
        rarity TEXT,
        source_site TEXT NOT NULL,
        collection_date TEXT NOT NULL,
        value REAL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    );
    """

    cursor.execute(create_table_user)

    cursor.execute(create_table_skins)


    conn.commit()

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

finally:

    if conn:
        conn.close()