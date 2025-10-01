import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd
from selenium.webdriver.common.keys import Keys

from utils import keydrop, skinclub, csgoskins

options = uc.ChromeOptions()

driver = uc.Chrome(options = options, version_main=140)



sheet = pd.read_excel('BOT-SKINS.xlsx')

for i, row in sheet.iterrows():

    if row['LINK'] == 'https://csgo-skins.com/case/daily-case':
        driver.get(row['LINK'])
        driver.maximize_window()
        sheet.loc[i, 'AWARD'] = csgoskins(driver, row)
