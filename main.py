import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import pandas as pd
from selenium.webdriver.common.keys import Keys

from utils import keydrop, skinclub, csgoskins, search_active_users

options = uc.ChromeOptions()

driver = uc.Chrome(options = options, version_main=142)


list_users = search_active_users()

for row in list_users:

    driver.get('https://csgo-skins.com/case/daily-case')
    driver.maximize_window()
    csgo_skins = csgoskins(driver, row)
    

    # driver.get('https://key-drop.com/pt/daily-case/level/0')
    # driver.maximize_window()
    # csgo_skins = keydrop(driver, row)
