from bs4 import BeautifulSoup
  
# HTML Document
new = """
        <item>
            <title>VPS 1</title>
        </item>
        <item>
            <title>VPS 2</title>
        </item>
        <item>
            <title>VPS 3</title>
        </item>
        """

old = """
        <item>
            <title>VPS 1</title>
        </item>
        <item>
            <title>VPS 2</title>
        </item>
        <item>
            <title>VPS 3</title>
        </item>
        """

update = """
        <item>
            <title>VPS SNERT</title>
        </item>
        <item>
            <title>VPS 2</title>
        </item>
        <item>
            <title>VPS 3</title>
        </item>
        """

soup_new = BeautifulSoup(new, 'html.parser')
soup_old = BeautifulSoup(old, 'html.parser')
soup_update = BeautifulSoup(update, 'html.parser')

items_new = soup_new.find_all('item')
items_update = soup_update.find_all('item')
items_old = BeautifulSoup()

def whats_new(items_new):
    global items_old
    difference = list(set(items_old).symmetric_difference(set(items_new)))

    print("old input: ",items_old)
    print('================================')
    items_old = items_new
    print("newly set old", items_old)
    print('================================')

    print("whats actually new: ", difference)
    print('================================')
    #checks if item got removed 
    #for item in difference:
    #    if item in items_old:
    #        items_old.remove(item)
    




whats_new(items_new)
items_new = items_update
whats_new(items_new)

# to fix

# when adding an item while removing an item
# at the same time, result also retuns removed item
# 
# find solution to remove old content from overflow