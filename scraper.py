import imp
import requests
from bs4 import BeautifulSoup
import hashlib
from bot import embed

url = 'https://snerts.de/' #'https://www.netcup-sonderangebote.de/feed/'
items_old = BeautifulSoup()

def update():

    feed = requests.get(url)
    soup_feed = BeautifulSoup(feed.content, 'xml')
    items_new = soup_feed.find_all('item')

    check_update(items_new)



# returns the guid id of passed item
def get_guid_id(tag):
    guid = tag.find('guid').text
    id = guid.split('=')[-1]
    return id

# returns true if content has been updated.
# compares old and new hash by hashing all guid id's
current_hash = str()
def check_update(items_new):
    global current_hash
    guid_sum = str()
    for item in items_new:
        guid_sum += get_guid_id(item)

    new_hash = hashlib.sha224(guid_sum.encode('utf-8')).hexdigest()

    if new_hash == current_hash:
        print('No Updates')
    else:
        current_hash = new_hash
        # what to happen when update got detected
        build_message(whats_new(items_new))

def build_message(items_output):
    for item in items_output:
        embed('test','test','test','test')

    
# returns items that got added this iteration
def whats_new(items_new):
    global items_old
    final = BeautifulSoup()

    for new_item in items_new:
        if new_item not in items_old:
            final.append(new_item)
    
    items_old = items_new
    return final

