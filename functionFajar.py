from functionAlfa import tablelize

def validateUserSelection(listMenu, userSelection):
  listOfCode = []
  # Bikin list buat nampung semua kode menu yang ada
  for menu in listMenu:
    listOfCode.append(menu['Kode Menu'])
  
  # Cek apakah yang dipilih user ada di list code apa engga
  if userSelection not in listOfCode:
    return False 
  else:
    return True
  
def showMenu(menu):
  # buat variabel buat nampung menu makanan dan minumannya
  makanan = []
  minuman = []
  
  # menunya di looping
  for data in menu:
    
    # kalo typenya makanan, bakal dimasukin ke list makanan
    if data['Type'] == 'makanan':
      makanan.append(data)
    else :
      # Kalo typenya minuman, bakal dimasukin ke list minuman
      minuman.append(data)
  
  tablelize(makanan, 'rounded_grid')
  tablelize(minuman, 'rounded_grid')