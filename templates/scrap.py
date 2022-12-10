from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('dax.csv','w')
csv_writer = csv.writer(csv_file)


src = requests.get('https://www.theguardian.com/international').text
soup = BeautifulSoup(src,'lxml')
list_t = list()
for art in soup.find_all('div',class_='fc-item__container'):
    tool = art.a.text
    csv_writer.writerow([tool])
    list_t.append(tool)

print (list_t)
