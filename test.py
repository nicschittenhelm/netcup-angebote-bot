import requests
from bs4 import BeautifulSoup
import hashlib
  
# HTML Document
new = '''
        <item>
            <title>VPS 1</title>
            <guid isPermaLink="false">https://www.netcup-sonderangebote.de/?p=2799</guid>
        </item>
        <item>
            <title>VPS 2</title>
            <guid isPermaLink="false">https://www.netcup-sonderangebote.de/?p=2779</guid>
        </item>
        <item>
            <title>VPS 3</title>
            <guid isPermaLink="false">https://www.netcup-sonderangebote.de/?p=5799</guid>
        </item>
        '''

old = '''
        <item>
            <title>VPS 1</title>
            <guid isPermaLink="false">https://www.netcup-sonderangebote.de/?p=2799</guid>
        </item>
        <item>
            <title>VPS 2</title>
            <guid isPermaLink="false">https://www.netcup-sonderangebote.de/?p=2779</guid>
        </item>
        <item>
            <title>VPS 3</title>
            <guid isPermaLink="false">https://www.netcup-sonderangebote.de/?p=5799</guid>
        </item>
        '''

update = '''
        <item>
            <title>VPS NEU</title>
            <guid isPermaLink="false">https://www.netcup-sonderangebote.de/?p=9999</guid>
        </item>
        <item>
            <title>VPS 2</title>
            <guid isPermaLink="false">https://www.netcup-sonderangebote.de/?p=2779</guid>
        </item>
        <item>
            <title>VPS 3</title>
            <guid isPermaLink="false">https://www.netcup-sonderangebote.de/?p=5799</guid>
        </item>
        '''

soup_new = BeautifulSoup(new, 'html.parser')
soup_old = BeautifulSoup(old, 'html.parser')
soup_update = BeautifulSoup(update, 'html.parser')

items_new = soup_new.find_all('item')
items_update = soup_update.find_all('item')
items_old = BeautifulSoup()
    
def whats_new(items_new):
    global items_old
    final = BeautifulSoup()

    # for debugging
    print('old input: ',items_old)
    print('================================')
    print('new input: ',items_new)
    print('================================')

    for new_item in items_new:
        if new_item not in items_old:
            final.append(new_item)
    
    items_old = items_new

    print('final: ',final)
    print('================================')



# whats_new(items_new)
# items_new = items_update
# whats_new(items_new)

def get_guid_id(tag):
    guid = tag.find('guid').text
    id = guid.split('=')[-1]
    return id

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


print(check_update(items_new))
print(check_update(items_new))
items_new = items_update
print(check_update(items_new))
print(check_update(items_new))
print(check_update(items_new))
print(check_update(items_new))