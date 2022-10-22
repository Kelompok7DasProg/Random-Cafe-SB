listMakanan = [
  {
    'No': '1', 
    'Nama':'Nasigoreng', 
    'Harga': 15000
  },
  {
    'No': '2', 
    'Nama':'Bakso', 
    'Harga': 20000
  },
  {
    'No': '3', 
    'Nama': 'Pizza', 
    'Harga': 50000
  },
  {
    'No': '4', 
    'Nama': 'Bubur Ayam', 
    'Harga': 10000
  }
]

def selectMenu(listMenu, no):
  selectedMenu = ''
  for menu in listMenu:
    noMenu = menu.get('No')
    # print(noMenu)
    # print(menu)
    if noMenu == no:
      selectedMenu = menu
  
  return selectedMenu

menuOrder = selectMenu(listMakanan, '1')
print(menuOrder)