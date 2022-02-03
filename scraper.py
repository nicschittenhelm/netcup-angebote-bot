from doctest import DebugRunner
from tabnanny import check
import requests
from bs4 import BeautifulSoup

url = f'http://127.0.0.1:5500/netcup%20Sonderangebote.html'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
cards = soup.find_all('div', {'class':'card'})
available_cards = []
unavailable_class = 'card--unavailable'

def remove_unavailable (cards):
    for card in cards:

        unavailable = str(card).find(unavailable_class)
        if unavailable == -1:
            available_cards.append(card)

remove_unavailable(cards)   



title_div = available_cards[0].find('div', {'class':'card--content--title'})

for span in title_div.findAll('span'):
    span.replace_with('')

title = title_div.text


print(title)
