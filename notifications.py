import requests
import sqlite3

def search_active_sites(id):

    DB_FILE = "my_inventory.db"

    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row  
    cursor = conn.cursor()

    cursor.execute("SELECT id, site_link, telegram_token, chat_id, message_thread_id FROM sites WHERE id = ?;", (id,))
    
    row = cursor.fetchone()
    conn.close()
    return row



def send_telegram_message(id, menssage):
    
    telegram = search_active_sites(id)                    


    url_api = f"https://api.telegram.org/bot{telegram['telegram_token']}/sendMessage"

    payload = {
        "chat_id": telegram['chat_id'],
        "text": menssage,
        "message_thread_id": telegram['message_thread_id']
    }


    try:
        response = requests.post (url_api, json=payload)

        if response.status_code == 200:
            print("Message sent successfully.")
            return True
        else:
            print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")
            return False
    
    except Exception as e:
        print(f"An error occurred while sending the message: {e}")
        return False
    
