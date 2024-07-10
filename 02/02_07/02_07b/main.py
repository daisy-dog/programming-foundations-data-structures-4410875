# Linear Search

my_list = [8,5,0,3,9,7]
ITEM = 7

def search(item, listy):
  for element in listy:
    if element == item:
      return True
  return False

if (search(ITEM,my_list)):
  print("I found it!")

# ITEM_INDEX = my_list.index([ITEM])
ITEM_INDEX = my_list.index(ITEM)
print(ITEM_INDEX)