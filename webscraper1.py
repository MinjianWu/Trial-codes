from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.bbc.co.uk/news/uk-politics-54925322').text
soup = BeautifulSoup(source, 'lxml')
print(soup.prettify())

article = soup.find('title').text
print(article)
