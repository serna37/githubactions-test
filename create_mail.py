from google.oauth2.service_account import Credentials
import gspread
import datetime

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

# シートから、スクレイピングした結果を取得する
key = "XXX-SPREAD-SHEET-KEY-SAMPLE"
book = getSpreadSheet(key)
sheet = book.worksheet("sample-sheet")
val = sheet.acell('A3').value or 'no data'

# メールテンプレートを読み込む
with open('mail-template.html', 'r') as f:
    data_lines = f.read()

# 文字列置換で、変数をセットする
data_lines = data_lines.replace("TEMPLATE_1", val)
data_lines = data_lines.replace("TEMPLATE_2", datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
data_lines = data_lines.replace("TEMPLATE_3", "なんか")

# 送る用ファイル sendmail に書き込む
with open('sendmail.html', 'w') as f:
    f.write(data_lines)
