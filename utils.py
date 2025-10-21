from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
from notifications import send_telegram_message
import pickle
import sqlite3
import datetime

locator = {
    # Key-Drop
    'join_keydrop': (By.XPATH, '//*[@id="app-root"]/header/div/div[2]/a'),
    'login_keydrop': (By.XPATH, '/html/body/reach-portal/div[3]/div/div/div/div/div/div[2]/div[2]/button'),
    'close_sell': (By.XPATH, '/html/body/div[8]/div/div/div/div[2]/div/div[3]/div[2]/button[1]'),
    'reward_keydrop': (By.XPATH,'/html/body/div[1]/main/div[3]/ul/li[1]/button/div/div/canvas'),

    # Steam
    'username_input': (By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[1]/input'),
    'password_input': (By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[2]/input'),
    'login_steam': (By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[4]'),

    # Skin-Club
    'box_skinclub': (By.XPATH,'/html/body/div[1]/div/div[5]/div/div[3]/a[1]/div/div'),
    'reward_skinclub': (By.XPATH,'/html/body/div[1]/div/div[5]/div[1]/div[3]/div/button'),

    # CSGO-SKINS
    'box_csgoskins': (By.XPATH,'/html/body/div[1]/div/div/main/div/section[1]/div[2]/div[1]/button'),
    'reward_csgoskins': (By.XPATH,'/html/body/div[1]/div/div/main/div/section[1]/div[1]/div/div[2]/div/ul/li[42]/div[1]'),
    'item_div': (By.CSS_SELECTOR,'#__layout > div > main > div > section.AppPage_section.section--control > div.section_tapes > div > div.ContainerTape.ContainerTape--list-ended > div > ul > li.ContainerTape_item.item--featured.item--won > div.item_name'),
    'skin_name': (By.XPATH,'/html/body/div[1]/div/div/main/div/section[1]/div[1]/div/div[2]/div/ul/li[42]/div[1]/span'),
    'value_item': (By.XPATH,'/html/body/div[1]/div/div/main/div/section[1]/div[2]/div[1]/button[1]/span/span'),
    'csgoskins': (By.XPATH,'/html/body/div[1]/div/div/header/div/div[1]/a')
}

def save_cookies(driver, file):
    with open(file, "wb") as f:
        pickle.dump(driver.get_cookies(), f)

def load_cookies(driver,file):
    with open(file, "rb") as f:
        cookies = pickle.load(f)

    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.refresh()

def saving_on_database(gun_name, skin_name, user_id, value, rarity, website):
    db_file = "my_inventory.db"
    conn = None

    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()


        rarity_check = rarity if rarity else "Rarity not defined"
        source_site = website if website else "Website not defined"
        

        collection_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


        sql_insert = """
            INSERT INTO skins 
            (gun_name, skin_name, rarity, source_site, collection_date, value, user_id) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        

        dados_da_skin = (gun_name, skin_name, rarity_check, source_site, collection_date, value, user_id)

        cursor.execute(sql_insert, dados_da_skin)
        
        conn.commit()
        


    except sqlite3.Error as e:
        print(f"❌ Erro ao inserir dados no banco de dados: {e}")

    finally:
        if conn:
            conn.close()

def search_active_users ():

    DB_FILE = "my_inventory.db"

    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row  
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, steam_id, nome_perfil, email, password FROM users")
    
    list_users = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return list_users


def keydrop(driver, row):

    # sleep(5)
    # save_cookies(driver, "cookies_key-drop.pkl")



    load_cookies(driver, "cookies_key-drop.pkl")

    sleep(5)

    redeem_buttom = driver.find_element(*locator['reward_keydrop'])
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", redeem_buttom)

    try:
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(locator['close_sell'])).click()
    except:
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(locator['reward_keydrop'])).click()

    # item_name
    # rarity 
    # value


    sleep(5)





    return "AWARD"

def skinclub(driver, row):

    # sleep(5)
    # save_cookies(driver, "cookies_skinclub.pkl")



    # load_cookies(driver, "cookies_skinclub.pkl")

    sleep(5)

    redeem_buttom = driver.find_element(*locator['box_skinclub'])
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", redeem_buttom)

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable(locator['box_skinclub'])).click()

    redeem_buttom = driver.find_element(*locator['reward_skinclub'])
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", redeem_buttom)

    sleep(2)

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable(locator['reward_skinclub'])).click()

    sleep(5)



    # item_name
    # rarity 
    # value


    sleep(5)





    return "AWARD"

def csgoskins(driver, row):


    try:

        sleep(5)

        load_cookies(driver, "csgoskins.pkl")

        sleep(10)

        redeem_buttom = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator['box_csgoskins']))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", redeem_buttom)

        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(locator['box_csgoskins'])).click()

        sleep(2)

        skin_name = WebDriverWait(driver, 30).until(EC.presence_of_element_located(locator['skin_name'])).text

        item_div = WebDriverWait(driver, 30).until(EC.presence_of_element_located(locator['item_div']))

        script_js = """
        const element = arguments[0];
        const childNodes = element.childNodes;
        const textNodes = [];

        for (let i = 0; i < childNodes.length; i++) {
            if (childNodes[i].nodeType === 3 && childNodes[i].textContent.trim() !== '') {
                textNodes.push(childNodes[i].textContent.trim());
            }
        }

        return textNodes;"""

        texts = driver.execute_script(script_js, item_div)


        gun_name = texts[0] if len(texts) > 0 else "Not found"
        rarity = texts[1] if len(texts) > 1 else "Not found"

        value_item = WebDriverWait(driver, 30).until(EC.presence_of_element_located(locator['value_item'])).text


        try:
            saving_on_database(gun_name, skin_name, row['id'], value_item, rarity, "CSGO-SKINS")

        except Exception as e:        
            print(f"Error saving to database: {e}")


        try:
            reward = {
                'gun_name': gun_name,
                'skin_name': skin_name,
                'rarity': rarity,
                'value_item': value_item
            }

            send_telegram_message(1, reward)
            print("✅ Reward captured and notification sent.")



        except Exception as e:
            print(f"Error creating reward dictionary: {e}")

    except Exception as e:
        print(f"Error capturing skin: {e}")
        saving_on_database('...', '...', '...', '...', '...', "CSGO-SKINS")

    finally:
        driver.quit()

