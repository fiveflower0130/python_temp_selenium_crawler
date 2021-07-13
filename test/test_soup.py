import requests
from requests.packages import urllib3
from bs4 import BeautifulSoup

root_url = 'https://myhr.kh.asegroup.com/HRIS/ATD/Discipline/Prevention?im=a'

urllib3.disable_warnings()
r = requests.get(root_url, verify=False)
print('r: ',r.status_code)
soup = BeautifulSoup(r.text, 'html.parser')

print('soup: ',soup)