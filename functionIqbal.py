def restrictedInput(text, restrictedText, choicesList, inputType):
  userInput = inputType(input(text))
  while userInput.lower() not in choicesList:
    print(restrictedText)
    userInput = inputType(input(text))
  
  return userInput.lower()

def selectMenu(listMenu, no):
  selectedMenu = ''
  for menu in listMenu:
    noMenu = menu.get('No')
    if noMenu == no:
      selectedMenu = menu
  
  return selectedMenu

def cancelPesanan(listPembelian):
  noBatal = restrictedInput('ingin batalkan pesanan no: ', 'input yang tesedia hanya no menu', ['1', '2', '3'], str)
  for i in range(len(listPembelian)):
    if listPembelian[i]['No'] == noBatal:
        del listPembelian[i]
        break

def pesan(listMakanan, listMinuman, listPembelian):
  tipeUser = restrictedInput('ingin beli makanan/minuman: ', 'input yang tesedia hanya makanan/minuman !!', ['makanan', 'minuman'], str)
  userOrder = {}
  
  if tipeUser == 'makanan':
    pilihanUser = input('Masukan no menu: ')
    quantityPembelian = int(input('Jumlah pembelian: '))
    menuUser = selectMenu(listMakanan, pilihanUser)
    
    userOrder['No'] = str(len(listPembelian) + 1)
    userOrder['Menu'] = menuUser['Nama']
    userOrder['Harga'] = menuUser['Harga']
    userOrder['Quantity'] = quantityPembelian
    userOrder['Type'] = ''
    
  elif tipeUser == 'minuman':
    pilihanUser = input('Masukan no menu: ')
    quantityPembelian = int(input('Jumlah pembelian: '))
    
    menuUser = selectMenu(listMinuman, pilihanUser)
    
    userOrder['No'] = str(len(listPembelian) + 1)
    userOrder['Menu'] = menuUser['Nama']
    userOrder['Harga'] = menuUser['Harga']
    userOrder['Quantity'] = quantityPembelian
  
  listPembelian.append(userOrder)
  
def batalSatuPesanan(listPembelian):
  cancelPesanan(listPembelian)
  print('Pesanan dibatalkan !')
  
  batalLagiGa = restrictedInput('Ingin batalkan pesanan lagi? Y/N: ', 'Input yang tersedia hanya Y/N', ['y', 'n'], str)
  
  while batalLagiGa == 'y':
    cancelPesanan(listPembelian)
    batalLagiGa = restrictedInput('Ingin batalkan pesanan lagi? Y/N: ', 'Input yang tersedia hanya Y/N', ['y', 'n'], str)
  
