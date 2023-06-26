from flask import Flask, request, render_template
import functions 
import sys
import imp
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

credentials_file_path = r"C:\Users\PC-2301007\Downloads\flilttoproject0912-feea31638bb6.json"
spreadsheet_key = '1k0_xoBUwtZBKS3oQg0KeJe0ukT40mflAHrWgR0i935U'#고정 

application = Flask(__name__)


@application.route('/', methods=['GET', 'POST'])
def input_html_function():
    return render_template('index.html')

@application.route('/input_data', methods=['GET', 'POST'])
def input_data_function():
    credentials_file_path = r"C:\Users\PC-2301007\Downloads\flilttoproject0912-feea31638bb6.json"
    spreadsheet_key = '1k0_xoBUwtZBKS3oQg0KeJe0ukT40mflAHrWgR0i935U'

    if request.method == 'POST':
        uid = request.form['uid']
        pwd = request.form['pwd']
        destination = request.form['destination']
        input_event = request.form['input_event']
        year = request.form['year']
        month = request.form['month']
        start_day = request.form['start_day']
        end_day = request.form['end_day']
        
        #run_webdriver(uid, pwd, destination, input_event, year, month, start_day, end_day)
    
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://a3.flit.to/")


        functions.login(driver, uid, pwd)
        functions.select_destination(destination)
        return_df = functions.select_date(input_event)
        spreadsheet = functions.open_spreadsheet(credentials_file_path, spreadsheet_key)
        target_worksheet = functions.get_worksheet(spreadsheet, input_event)
        functions.write_values(spreadsheet,target_worksheet, return_df, input_event)

        return render_template('outer.html', uid=uid, pwd=pwd, destination=destination, input_event=input_event, year=year, month=month, start_day=start_day, end_day=end_day)
    
    return render_template('index.html')







if __name__ == '__main__':
    application.run(host='0.0.0.0')