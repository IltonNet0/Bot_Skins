from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

locator = {
    'home': (By.XPATH, '//*[@id="app-root"]/header/div[1]/a')
}

def keydrop(driver, row):
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator['home'])).click()
    sleep(5)
    return "AWARD"