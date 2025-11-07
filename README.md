# 🎮 CS:GO Daily Skins Bot

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-Automation-success.svg)](https://www.selenium.dev/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey.svg)](https://www.sqlite.org/)
[![Telegram API](https://img.shields.io/badge/Telegram-Bot%20API-26A5E4.svg)](https://core.telegram.org/bots/api)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

> **CS:GO Daily Skins Bot** automates daily skin collections from multiple CS:GO case-opening websites and sends Telegram notifications with the captured rewards.

---

## 🚀 Features

- 🧠 **Automated Browser Interaction**  
  Uses `undetected_chromedriver` with Selenium to simulate user actions and open daily cases automatically.

- 💾 **Local Data Storage**  
  Stores all captured skins (weapon, skin name, rarity, value, and source) in an SQLite database (`my_inventory.db`).

- 🔔 **Telegram Notifications**  
  Sends real-time messages via the Telegram Bot API when a new skin is obtained.

- 👤 **Multi-User Support**  
  Each collected skin is linked to a registered user in the database.

- 🧱 **Modular Structure**  
  Organized into modules for database creation, Telegram notifications, scraping logic, and helper utilities.

---

## 🧩 Project Structure

```
.
├── create_database.py    # Creates the SQLite database and tables
├── main.py               # Entry point that runs the automation process
├── notifications.py      # Handles Telegram message sending
├── utils.py              # Utility functions for scraping, cookies, and DB operations
└── my_inventory.db       # SQLite database (created automatically)
```

---

## ⚙️ How It Works

1. **Database Setup**  
   Run `create_database.py` to generate `my_inventory.db` with all necessary tables.

2. **Automation Start**  
   Run `main.py` to launch the browser and start collecting daily rewards.  
   The script:
   - Loads cookies for each website.
   - Simulates button clicks to open cases.
   - Extracts weapon, skin, rarity, and value.
   - Saves results in the database.
   - Sends a Telegram message with the obtained skin info.

3. **Notifications**  
   `notifications.py` sends messages using the Telegram Bot API with the stored bot credentials.

---

## 🧠 Requirements

- Python **3.9+**
- Google Chrome (compatible with `undetected_chromedriver`)
- Install dependencies:
  ```bash
  pip install undetected-chromedriver selenium pandas requests
  ```

---

## 🧾 Example Telegram Message

```
🎉 New Skin Captured!

Gun: AK-47  
Skin: Redline  
Rarity: Classified  
Value: $7.25
```

---

## 💬 Setting Up Telegram Notifications

Follow these steps to configure Telegram message delivery:

### 1. Create a Telegram Bot
1. Open Telegram and start a chat with [@BotFather](https://t.me/BotFather).  
2. Send `/newbot` and follow the prompts.  
3. Copy the **token** that looks like this:
   ```
   123456789:ABCdefGHIjklMNOpqrSTUvwxYZ
   ```

---

### 2. Get Your Chat ID
1. Send any message to your new bot.  
2. Open this URL (replace `<TOKEN>` with your bot’s token):  
   ```
   https://api.telegram.org/bot<TOKEN>/getUpdates
   ```
3. In the JSON response, find `"chat":{"id":YOUR_CHAT_ID}` — that’s your **chat_id**.

---

### 3. Insert Bot Info into the Database
Once your database (`my_inventory.db`) is created, add your Telegram bot info:

```sql
INSERT INTO sites (site_link, telegram_token, chat_id, message_thread_id)
VALUES ('https://csgo-skins.com', '<YOUR_TELEGRAM_TOKEN>', '<YOUR_CHAT_ID>', NULL);
```

---

### 4. Test Your Bot
Run the test below to check if the bot sends messages correctly:

```python
from notifications import send_telegram_message
send_telegram_message(1, "✅ Telegram bot connected successfully!")
```

If you receive the message in your Telegram chat, it’s working perfectly.

---

## ⚠️ Notes

- ⚙️ Use automation responsibly — websites may limit automated access.  
- 🔐 Keep your credentials private (never commit `.pkl` or token files).  
- 🧩 Ensure valid cookies for each site before running the bot.  

---

## 📜 License

This project is licensed under the **MIT License** — you’re free to modify and use it as you wish.

---

## 💡 Author

**IltonNet**  
🔗 [GitHub Profile](https://github.com/IltonNet0)
