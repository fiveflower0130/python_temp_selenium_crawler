import requests
import time
import datetime
from requests.packages import urllib3
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from library.lib_function import Read_INI_File_Info

def get_browser_driver(name):
    if name == "chrome":
        return webdriver.Chrome('./browser_driver/chromedriver.exe')
    elif name == "ie":
        return webdriver.Ie('./browser_driver/IEDriverServer.exe')
    else:
        raise Exception("{0} is not supported.".format(name))

def get_url(name, id, pw):
    
    if name == "chrome":
        url = 'https://{0}:{1}@myhr.kh.asegroup.com/HRIS/ATD/Discipline/Prevention?im=a'.format(id, pw)
        return url
    elif name == "ie":
        url = 'https://myhr.kh.asegroup.com/HRIS/ATD/Discipline/Prevention?im=a'
        return url
    else:
        raise Exception("{0} is not supported url".format(name))
    
def auto_login(driver):
    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")

    username.send_keys("")
    password.send_keys("")

    driver.find_element_by_name("submit").click()

def run_action(browser):
    if browser:
        # 查詢上傳名單
        select_button = browser.find_element_by_id("btnSearch")
        select_button.click()
        time.sleep(12)

        # 選擇顯示50筆
        select = Select(browser.find_element_by_id("pageSizeSelect"))
        select.select_by_value('50')
        time.sleep(12)
    else:
        raise Exception("Can't run action, browser is empty or wrong.")

def get_url_soup(name, source):
    if source:
        if name == 'chrome':
            return BeautifulSoup(source, 'html.parser')
        elif name == 'ie':
            urllib3.disable_warnings()
            resp = requests.get(source, verify=False)
            if resp.status_code == 200:
                return BeautifulSoup(source, 'html.parser')
        else:
            raise ("{0} is not supported soup url".format(name))
    else:
       raise Exception("browser page source data is empty or wrong.") 

def get_data_processed(items, employees):
    real_data = []
    # 取得所需資料
    items_data = items[0]
    # 刪除不必要欄位
    del items_data[0:2]
    del employees[0]
    for data in employees:
        del data[0:2]
        # 轉換成dict
        dict_data = {items_data[i]: data[i] for i in range(len(items_data)) if items_data[i] == '量測日期' or items_data[i] == '進入門禁時間' or items_data[i] == '員工工號' or items_data[i] == '姓名' }
        real_data.append(dict_data)
    return real_data

def get_browser_data(name, source):
    soup = get_url_soup(name, source)
    items_data = []
    employees_data = []
    # 取得table資訊
    table = soup.find('table', attrs={'class': 'table table-sm table-hover table-bordered dataTable JPadding JColResizer'})
    # 取得table head and body資料並處理
    for row in table.findAll('tr'):
        item_cols = row.findAll('th')
        item_cols = [ele.text.strip() for ele in item_cols]
        items_data.append([ele for ele in item_cols])
        cols = row.findAll('td')
        cols = [ele.text.strip() for ele in cols]
        employees_data.append([ele for ele in cols]) # Get rid of empty values
    # 進行資料處理
    real_data = get_data_processed(items_data, employees_data)
    # 返回處理後資料
    return real_data

def output_data(result):
    if result:
        # 獲得當地時間
        datetime_dt = datetime.datetime.today()
        # 格式化日期
        datetime_str = datetime_dt.strftime("%Y-%m-%d-%H-%M-%S")
        file_name = "./output_data/{}.txt".format(datetime_str)
        with open(file_name, 'w', encoding="utf-8") as f:
            for item in result:
                f.write("量測日期: {0} 進入門禁時間: {1} 員工工號: {2} 姓名: {3} \n".format(item['量測日期'],item['進入門禁時間'],item['員工工號'],item['姓名']))
    else:
        raise Exception("output data {} is wrong or empty.".format(result))

def run_browser(name, id, password):
    try:
        # 取得browser driver
        browser= get_browser_driver(name)
        # 登入browser
        url = get_url(name, id, password)
        browser.get(url)
        # 執行動作
        run_action(browser)
        # 取得資料
        result_data = get_browser_data(name, browser.page_source)
        print(result_data)
        # 輸出結果
        output_data(result_data)
    except Exception as e:
        print("Error: ",e)
    finally:
        # 登出browser
        browser.quit()


def main():
    config = Read_INI_File_Info()
    browser_name = config.get('Driver', 'browser_driver')
    ase_id = config.get('LoginInfo', 'ase_id') #your ase id
    ase_password = config.get('LoginInfo', 'ase_password') # your ase password
    if ase_id and ase_password:
        run_browser(browser_name, ase_id, ase_password)
    else:
        raise Exception("id or password is empty or wrong.")    


if __name__ == '__main__':
    main()
