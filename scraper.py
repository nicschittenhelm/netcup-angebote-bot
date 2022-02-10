import requests
from bs4 import BeautifulSoup
import bs4
import hashlib
import re

# stores hash of previous iteration
current_hash = str()
# stores all items from previous iteration
items_old = BeautifulSoup()

class RunScraper:

    def __init__(self):
        self.url = 'https://snerts.de/' #'https://www.netcup-sonderangebote.de/feed/'
        self.feed = requests.get(self.url)
        self.soup_feed = BeautifulSoup(self.feed.content, 'html.parser')
        self.items_new = self.soup_feed.find_all('item')

    def __del__(self):
        print('instance deleted')

    # returns the guid id of passed item
    def get_guid_id(self, tag):
        guid = tag.find('guid').text
        id = guid.split('=')[-1]
        return id


    # returns true if content has been updated.
    # compares old and new hash by hashing all guid id's
    def check_update(self):
        global current_hash
        guid_sum = str()
        for item in self.items_new:
            guid_sum += self.get_guid_id(item)

        new_hash = hashlib.sha224(guid_sum.encode('utf-8')).hexdigest()

        if new_hash == current_hash:
            return False
        else:
            current_hash = new_hash
            return True


    # returns items that got added this iteration
    def whats_new(self):
        global items_old
        final = BeautifulSoup()

        for new_item in self.items_new:
            if new_item not in items_old:
                final.append(new_item)
        
        items_old = self.items_new
        return final


    def build_data(self, tag):
        data_item = {}
        data_item['title'] = tag.title.get_text()
        data_item['type'] = tag.category.get_text()
        data_item['price'] = self.get_price(tag.find('content:encoded'))
        data_item['link'] = tag.guid.get_text()

        return data_item

    # extracts data from CDATA and puts it in new soup
    # replaces 'EUR' with '€' to avoid returning 'None' due to inconsistent naming
    # finds price using regex
    def get_price(self, tag):
        CDATA = BeautifulSoup(tag.find(text=lambda tag: isinstance(tag, bs4.CData)).text.replace('EUR', '€'), 'html.parser')
        content = str(CDATA.find(string=re.compile('€')))

        return content
