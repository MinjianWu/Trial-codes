from bs4 import BeautifulSoup
import requests

source = requests.get('https://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

article = soup.find('header', class_='entry-header')
# print(article)

url_ = article.h2.a['href']
# print(url_)

content = soup.find('div', class_='entry-content').text
print(content)
