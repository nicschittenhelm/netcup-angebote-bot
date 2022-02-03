cards = ['eins','zwei','drei','vier']
string = 'zwei'

def snert(cards):
    for card in cards:
        if string in card:
            print('found')

snert(cards)