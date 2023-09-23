from bs4 import BeautifulSoup
import requests

rq = requests.get('https://catec.kz/vakansii')
soup = BeautifulSoup(rq.text, 'html.parser')

divan = soup.find('div', class_='col-md-12 page__content')
print(divan('p'))
