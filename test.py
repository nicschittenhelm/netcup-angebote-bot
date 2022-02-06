from bs4 import BeautifulSoup
  
# HTML Document
new = '''
        <item>
            <title>VPS 1</title>
        </item>
        <item>
            <title>VPS 2</title>
        </item>
        <item>
            <title>VPS 3</title>
        </item>
        '''

old = '''
        <item>
            <title>VPS 1</title>
        </item>
        <item>
            <title>VPS 2</title>
        </item>
        <item>
            <title>VPS 3</title>
        </item>
        '''

update = '''
        <item>
            <title>VPS NOCH TEURER</title>
        </item>
        <item>
            <title>VPS ZU TEUER</title>
        </item>
        <item>
            <title>VPS 2</title>
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



whats_new(items_new)
items_new = items_update
whats_new(items_new)
