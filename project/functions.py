import gspread
import gspread_dataframe
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials
from gspread_dataframe import set_with_dataframe
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common import keys
from datetime import date
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pandas as pd
from bs4 import BeautifulSoup
import re
import os

def generate_date_range(year, month, start_day, end_day):
    start_date = date(year, month, start_day).isoformat()
    end_date = date(year, month, end_day).isoformat()
    return start_date, end_date

def login(driver, uid, pwd):
    
    id_box = driver.find_element(by=By.NAME, value="email")
    pw_box = driver.find_element(by=By.NAME, value="password")
    login = driver.find_element(by=By.CLASS_NAME, value="btn")
    
    id_box.click()
    
    id_box.send_keys(uid)
    pw_box.send_keys(pwd)
    login.click()
    
    time.sleep(10)

def select_destination(destination):
    nextpage = driver.find_elements(by=By.CSS_SELECTOR, value='.action-children a[href]')
    dest_options = [n.text for n in nextpage]
    
    #if destination in dest_options:
    driver.find_element(by=By.LINK_TEXT, value= destination ).click()

def get_dataframe():
    time.sleep(2)
    html = driver.page_source
    df = pd.read_html(html)[-1]
    print(df)
    print('get_dataframe')
    return df

def select_date(input_event):
    time.sleep(2)
    button = driver.find_element(By.XPATH, "//button[contains(text(), 'View Statistics')]")
    button.click()
    select_element = driver.find_elements(By.CSS_SELECTOR, "select.form-control")
    
    #pushing select 
    driver.find_elements(by=By.XPATH, value='//select')[-1].click()
    
    #get all events
    options = driver.find_elements(by=By.XPATH, value='//option') # Event options 가져옴
    events = [opt.text for opt in options if re.match('^[0-9]{3}[.]?', opt.text)] 
    
    if input_event in events:
        driver.find_elements(by=By.XPATH, value='//select')[-1].click()
        driver.find_element(by=By.XPATH, value=f'//option[contains(text(), "{input_event}")]').click()
        
        #date 
        start_date, end_date = generate_date_range(year, month, start_day, end_day)
        new_date = f'{start_date} - {end_date}'
        
        date_select = driver.find_element(by=By.NAME, value='date-range-input') # 날짜 입력창
        time.sleep(2)

        date_select.click()
        date_select.send_keys(keys.Keys.BACKSPACE * len(new_date), new_date, keys.Keys.ENTER) # 날짜 입력창 선택 >> Backspace로 지우기 >> 다시 쓰기

        time.sleep(2)
        df = get_dataframe()
       
    return df   

def open_spreadsheet(credentials_file_path, spreadsheet_key):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets']
    credentials = Credentials.from_service_account_file(credentials_file_path, scopes=scope)
    client = gspread.authorize(credentials)

    # 스프레드시트 열기
    spreadsheet = client.open_by_key(spreadsheet_key)
    print(spreadsheet)
    return spreadsheet

def get_worksheet(spreadsheet, input_event):
    
    numbers = re.findall(r'\d+', input_event)

    target_worksheet = None
    
    worksheets = spreadsheet.worksheets()
    
    for worksheet in worksheets:
        title = worksheet.title
        numbers_in_title = re.findall(r'\d+', title)
        if len(numbers_in_title) == 1 and len(numbers) == 1:  # 리스트가 비어있지 않은지 확인
            if numbers[0] == numbers_in_title[0]:
                target_worksheet = worksheet
                print(target_worksheet)
                break 
        elif numbers and numbers_in_title:  # 리스트가 비어있지 않은지 확인
            if numbers[0] == numbers_in_title[0]:
                target_worksheet = worksheet
                print(target_worksheet)
                break 
        if target_worksheet is not None:
            break 
            
    return target_worksheet
            
def write_values(spreadsheet,target_worksheet, df, input_event):
    if target_worksheet is None:
        print("Target worksheet not found")
    else:
        print(target_worksheet)
    if len(df) == 1:
        print('There is no data')
    else:
        column_values = target_worksheet.col_values(3)
        range_column = len(column_values) + 1 
        target_worksheet.update(f'C{range_column}:L',df[:-1].values.tolist())
        print("write_values")

'''
uid = "jeongwoo.yoon@flitto.com" # 비타민 아이디/이메일
pwd = '000000' # 비타민 비밀번호
destination = 'internal-user-management'
input_event = '476. [Internal][24-7 Services]::[ko-th] NIKL CO'
year = 2022
month = 10
start_day = 1
end_day = 22
#credentials_file_path = os.path.abspath('')+ "\\"+ 'flilttoproject0912-feea31638bb6.json'
credentials_file_path = r"C:\Users\PC-2301007\Downloads\flilttoproject0912-feea31638bb6.json"
spreadsheet_key = '1k0_xoBUwtZBKS3oQg0KeJe0ukT40mflAHrWgR0i935U'#고정 




chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://a3.flit.to/")


login(driver, uid, pwd)
select_destination(destination)
return_df = select_date(input_event)
spreadsheet = open_spreadsheet(credentials_file_path, spreadsheet_key)
target_worksheet = get_worksheet(spreadsheet, input_event)
write_values(spreadsheet,target_worksheet, return_df, input_event)'''
