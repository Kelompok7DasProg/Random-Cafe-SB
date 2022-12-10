from functionAlfa import tablelize

def validateUserSelection(listMenu, userSelection):
  listOfCode = []
  for menu in listMenu:
    listOfCode.append(menu['Kode Menu'])
  
  if userSelection not in listOfCode:
    return False 
  else:
    return True
  
def showMenu(menu):
  makanan = []
  minuman = []
  
  for data in menu:
    if data['Type'] == 'makanan':
      makanan.append(data)
    else :
      minuman.append(data)
  
  tablelize(makanan, 'rounded_grid')
  tablelize(minuman, 'rounded_grid')