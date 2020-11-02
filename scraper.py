import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.sportinglife.com/football/live')

result = BeautifulSoup(r.text, 'html.parser')
print(result.find('Leeds United'))

string = 'name":"Leeds United","short_name":"Leeds"},"score":'

#if "leeds" in r.text:
#    for line in r.text.split('\n'):
#        if string in line:
#            print(line)
#else:
#    print("leeds not found")#
