import requests
import sqlite3

def search_active_sites(id):

    DB_FILE = "my_inventory.db"

    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row  
    cursor = conn.cursor()

    cursor.execute("SELECT id, site_link, telegram_token, chat_id, message_thread_id FROM sites WHERE id = ?;", (id))
    
    row = cursor.fetchall()
    conn.close()
    return row


def send_telegram_message(id, reward):
    
    telegram = search_active_sites(id)                    


