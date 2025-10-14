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
        gun_name TEXT NOT NULL,
        skin_name TEXT NOT NULL,
        rarity TEXT NOT NULL,
        source_site TEXT NOT NULL,
        collection_date TEXT NOT NULL,
        value REAL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    );
    """

    create_table_sites = """
    CREATE TABLE IF NOT EXISTS sites (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        site_link TEXT NOT NULL,
        telegram_token TEXT,
        chat_id TEXT,
        status TEXT NOT NULL
    );
    """


    cursor.execute(create_table_user)

    cursor.execute(create_table_skins)

    cursor.execute(create_table_sites)

    conn.commit()

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

finally:

    if conn:
        conn.close()