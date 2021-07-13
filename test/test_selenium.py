import requests
from requests.packages import urllib3
import time
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome('../browser_driver/chromedriver.exe')
browser.get('https://K09857:@WSXplmn34@myhr.kh.asegroup.com/HRIS/ATD/Discipline/Prevention?im=a')
select_button = browser.find_element_by_id("btnSearch")
# 執行查詢
select_button.click()
time.sleep(10)
# 選擇顯示50筆
select = Select(browser.find_element_by_id("pageSizeSelect"))
select.select_by_value('50')
time.sleep(10)
soup = BeautifulSoup(browser.page_source, 'html.parser')
items_data = []
employees_data = []
real_data = []
table = soup.find('table', attrs={'class': 'table table-sm table-hover table-bordered dataTable JPadding JColResizer'})

for row in table.findAll('tr'):
    item_cols = row.findAll('th')
    item_cols = [ele.text.strip() for ele in item_cols]
    items_data.append([ele for ele in item_cols])
    cols = row.findAll('td')
    cols = [ele.text.strip() for ele in cols]
    employees_data.append([ele for ele in cols]) # Get rid of empty values

items_data = items_data[0]
del employees_data[0]
del items_data[0:2]

for data in employees_data:
    del data[0:2]
    data_dict = {}
    for i in range(len(items_data)):
        if items_data[i] == '量測日期' or items_data[i] == '進入門禁時間' or items_data[i] == '員工工號' or items_data[i] == '姓名':
            data_dict[items_data[i]] = data[i]
    real_data.append(data_dict)

datetime_dt = datetime.datetime.today()# 獲得當地時間
datetime_str = datetime_dt.strftime("%Y-%m-%d-%H-%M-%S")  # 格式化日期
file_name = "../output_data/{}.txt".format(datetime_str)

with open(file_name, 'w', encoding="utf-8") as f:
    for item in real_data:
        f.write("%s\n" % item)
        # f.write("量測日期: {0} 進入門禁時間: {1} 員工工號: {2} 姓名: {3} \n".format(item['量測日期'],item['進入門禁時間'],item['員工工號'],item['姓名']))

browser.quit()