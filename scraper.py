import requests
from bs4 import BeautifulSoup
import hashlib


url = 'http://127.0.0.1:5500/feed.xml' #'https://www.netcup-sonderangebote.de/feed/'
feed = requests.get(url)
soup_feed = BeautifulSoup(feed.content, 'xml')

items_new = soup_feed.find_all('item')
items_old = BeautifulSoup()

# returns the guid id of passed item
def get_guid_id(tag):
    guid = tag.find('guid').text
    id = guid.split('=')[-1]
    return id

# returns true or false if content has updated.
# compares old and new hash by hashing all guid id's
current_hash = str()
def check_update(items_new):
    global current_hash
    guid_sum = str()
    for item in items_new:
        guid_sum += get_guid_id(item)
    
    new_hash = hashlib.sha224(guid_sum.encode('utf-8')).hexdigest()

    if new_hash == current_hash:
        return False
    
    current_hash = new_hash
    return True

#print(current_hash)
#print(check_update(items_new))
#print(current_hash)

def whats_new(items_new):
    global items_old
    difference = list(set(items_old).symmetric_difference(set(items_new)))
    print("differenz: " + str(len(difference)))
    print("alt: " + str(len(difference)))
    print(" ")

    items_old = items_new

    print("differenz: " + str(len(difference)))
    print("alt: " + str(len(difference)))
    print(" ")

    for item in difference:
        if item in items_old:
            items_old.remove(item)
    
    print("differenz: " + str(len(difference)))
    print("alt: " + str(len(difference)))
    print(" ")


whats_new(items_new)