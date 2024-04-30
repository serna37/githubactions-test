# サンプルです

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from google.oauth2.service_account import Credentials
import gspread
import datetime
from time import sleep

def getDriver():
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("enable-automation")
    options.add_argument("disable-infobars")
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-browser-side-navigation")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1980, 1040)
    return driver

# URLにアクセス
driver = getDriver()
driver.get("https://sample.sample.com/sample")
sleep(3)

# なんかID パスワードいれてログインボタン押すとする
driver.find_element(By.CSS_SELECTOR, "#sample-id").send_keys("sample")
driver.find_element(By.CSS_SELECTOR, "#sample-password").send_keys("sample")
driver.find_element(By.CSS_SELECTOR, "#sample-btn").click()
sleep(3)

# なんか値取得してみる
target = driver.find_element(By.CSS_SELECTOR, "#sample-selector")
txt = target.get_attribute("textContent")
result = target.text
driver.quit()


def getSpreadSheet(sheet_key):
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
    # サンプルなので動きません
    credentials = Credentials.from_service_account_file('サービスアカウントキー.json', scopes=scopes)
    gc = gspread.authorize(credentials)
    sh = gc.open_by_key(sheet_key)
    return sh

# スプレッドシートに書き込んでおく
key = "XXX-SPREAD-SHEET-KEY-SAMPLE"
book = getSpreadSheet(key)
sheet = book.worksheet("sample-sheet")
val_a1 = int(sheet.acell('A1').value or 0)
val_a1 += 1
print(val_a1)
sheet.update_acell('A2', datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
sheet.update_acell('A3', str(result))
