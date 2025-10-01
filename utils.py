from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import pickle
import sqlite3

locator = {
    # Key-Drop
    'join_keydrop': (By.XPATH, '//*[@id="app-root"]/header/div/div[2]/a'),
    'login_keydrop': (By.XPATH, '/html/body/reach-portal/div[3]/div/div/div/div/div/div[2]/div[2]/button'),
    'close_sell': (By.XPATH, '/html/body/div[8]/div/div/div/div[2]/div/div[3]/div[2]/button[1]'),
    'award_keydrop': (By.XPATH,'/html/body/div[1]/main/div[3]/ul/li[1]/button/div/div/canvas'),

    # Steam
    'username_input': (By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[1]/input'),
    'password_input': (By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[2]/input'),
    'login_steam': (By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[4]'),

    # Skin-Club
    'box_skinclub': (By.XPATH,'/html/body/div[1]/div/div[5]/div/div[3]/a[1]/div/div'),
    'award_skinclub': (By.XPATH,'/html/body/div[1]/div/div[5]/div[1]/div[3]/div/button'),

    # CSGO-SKINS
    'box_csgoskins': (By.XPATH,'/html/body/div[1]/div/div/main/div/section[1]/div[2]/div[1]/button'),
    'award_csgoskins': (By.XPATH,'/html/body/div[1]/div/div/main/div/section[1]/div[1]/div/div[2]/div/ul/li[42]/div[1]'),
    'item_div': (By.CSS_SELECTOR,'#__layout > div > main > div > section.AppPage_section.section--control > div.section_tapes > div > div.ContainerTape.ContainerTape--list-ended > div > ul > li.ContainerTape_item.item--featured.item--won > div.item_name'),
    'skin_name': (By.XPATH,'/html/body/div[1]/div/div/main/div/section[1]/div[1]/div/div[2]/div/ul/li[42]/div[1]/span'),
    'value_item': (By.XPATH,'/html/body/div[1]/div/div/main/div/section[1]/div[2]/div[1]/button[1]/span/span')
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

def salvar_skin_no_banco(nome, tipo_skin, cond):
    """Insere os dados de uma skin no banco de dados."""
    try:
        conn = sqlite3.connect('my_inventory.db')
        cursor = conn.cursor()
        sql_insert = "INSERT INTO skins (nome, tipo, condicao) VALUES (?, ?, ?)"
        dados_da_skin = (nome, tipo_skin, cond)
        cursor.execute(sql_insert, dados_da_skin)
        conn.commit()
        print(f"✅ Skin '{nome} - {cond}' salva no banco de dados com sucesso!")
    except sqlite3.Error as e:
        print(f"❌ Erro ao inserir dados no banco de dados: {e}")
    finally:
        if conn:
            conn.close()





def keydrop(driver, row):

    # sleep(5)
    # save_cookies(driver, "cookies_key-drop.pkl")



    load_cookies(driver, "cookies_key-drop.pkl")

    sleep(5)

    redeem_buttom = driver.find_element(*locator['award_keydrop'])
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", redeem_buttom)

    try:
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(locator['close_sell'])).click()
    except:
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(locator['award_keydrop'])).click()

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

    redeem_buttom = driver.find_element(*locator['award_skinclub'])
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", redeem_buttom)

    sleep(2)

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable(locator['award_skinclub'])).click()

    sleep(5)



    # item_name
    # rarity 
    # value


    sleep(5)





    return "AWARD"


def csgoskins(driver, row):

    sleep(5)


    load_cookies(driver, "csgoskins.pkl")

    redeem_buttom = driver.find_element(*locator['box_csgoskins'])
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", redeem_buttom)

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable(locator['box_csgoskins'])).click()

    item_div = driver.find_element(*locator['item_div'])

    skin_name = WebDriverWait(driver, 30).until(EC.presence_of_element_located(locator['skin_name'])).text

    script_js = """
    const element = arguments[0];
    const childNodes = element.childNodes;
    const textNodes = [];

    for (let i = 0; i < childNodes.length; i++) {
        if (childNodes[i].nodeType === 3 && childNodes[i].textContent.trim() !== '') {
            textNodes.push(childNodes[i].textContent.trim());
        }
    }

    return textNodes;
"""

    textos_soltos = driver.execute_script(script_js, item_div)


    gun_name = textos_soltos[0] if len(textos_soltos) > 0 else "Não encontrado"
    rarity = textos_soltos[1] if len(textos_soltos) > 1 else "Não encontrado"

    value_item = WebDriverWait(driver, 30).until(EC.presence_of_element_located(locator['value_item'])).text

    print(f"Nome da Skin: {skin_name}")
    print(f"Tipo: {gun_name}")
    print(f"Condição: {rarity}")


    sleep(5)
    # item_name
    # rarity 
    # value