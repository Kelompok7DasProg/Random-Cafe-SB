from copy import deepcopy
import random
import time
import tabulate

def randomPrice():
  randomInt = random.randint(5000, 40000)
  
  return round(randomInt,-3)

def restrictedInput(text, restrictedText, choicesList, inputType):
  userInput = inputType(input(text))
  while userInput.lower() not in choicesList:
    print(restrictedText)
    userInput = inputType(input(text))
  
  return userInput.lower()

def selectMenu(listMenu, kodeUser):
  selectedMenu = ''
  for menu in listMenu:
    kodeMenu = menu.get('Kode Menu')
    if kodeMenu == kodeUser:
      selectedMenu = menu
  
  return selectedMenu

def cancelPesanan(listPembelian):
  noBatal = input('Masukan kode menu yang ingin dibatalkan: ')
  
  validateUser = validateUserSelection(listPembelian, noBatal.upper())
  
  while validateUser != True:
    print('Kode menu yang diinput salah / tidak valid, silahkan coba lagi !!')
    
    noBatal = input('Masukan kode menu yang ingin dibatalkan: ')
    validateUser = validateUserSelection(listPembelian, noBatal.upper())
  
  for i in range(len(listPembelian)):
    if listPembelian[i]['Kode Menu'] == noBatal.upper():
      if listPembelian[i]['isRandom'] == True:
        print('Pesanan yang dari randomate tidak bisa dibatalkan !!!')
      else :
        del listPembelian[i]
        break

def deleteKey(listToDelete, key):
  
  listCopy = deepcopy(listToDelete)
  
  for listDict in listCopy:
    del listDict[key]
  
  return listCopy

def pesanSekali(listMenu, listPembelian):
  userOrder = {}
  tablelize(listMenu)
  
  pilihanUser = input('Masukan kode menu: ')
  
  validateUser = validateUserSelection(listMenu, pilihanUser.upper())
  
  while validateUser != True:
    print('Kode menu yang diinput salah / tidak valid, silahkan coba lagi !!')
    
    pilihanUser = input('Masukan kode menu: ')
    validateUser = validateUserSelection(listMenu, pilihanUser.upper())
  
  quantityPembelian = int(input('Jumlah pembelian: '))
  menuUser = selectMenu(listMenu, pilihanUser.upper())
    
  userOrder['Kode Menu'] = menuUser['Kode Menu']
  userOrder['Menu'] = menuUser['Nama']
  userOrder['Harga'] = int(menuUser['Harga'])
  userOrder['Quantity'] = quantityPembelian
  userOrder['Total harga'] = int(menuUser['Harga']) * quantityPembelian
  userOrder['isRandom'] = False
  
  listPembelian.append(userOrder)

def pesan(listMenu, listPembelian):
  randomateOffer = restrictedInput('Ingin menggunakan fitur randomate? Y/N', 'Input yang tersedia hanya Y/N !!', ['y','n'], str)
  
  if randomateOffer == 'y':
    randomateOrder(listMenu, listPembelian)
  else :
    pesanSekali(listMenu, listPembelian)
    
  orderLagi = restrictedInput('Ingin pesan lagi? Y/N: ', 'Input yang tersedia hanya Y/N !!', ['y','n'], str)

  while orderLagi == 'y':
    randomateOffer = restrictedInput('Ingin menggunakan fitur randomate? Y/N', 'Input yang tersedia hanya Y/N !!', ['y','n'], str)
    if randomateOffer == 'y':
      randomateOrder(listMenu, listPembelian)
    else :
      pesanSekali(listMenu, listPembelian)
      
    orderLagi = restrictedInput('Ingin pesan lagi? Y/N: ', 'Input yang tersedia hanya Y/N !!', ['y','n'], str)
  
def batalPesan(listPembelian):
  tablelize(listPembelian)
  cancelPesanan(listPembelian)
  print('Pesanan dibatalkan !')
  
  batalLagiGa = restrictedInput('Ingin batalkan pesanan lagi? Y/N: ', 'Input yang tersedia hanya Y/N', ['y', 'n'], str)
  
  while batalLagiGa == 'y':
    cancelPesanan(listPembelian)
    batalLagiGa = restrictedInput('Ingin batalkan pesanan lagi? Y/N: ', 'Input yang tersedia hanya Y/N', ['y', 'n'], str)
  
def randomateOrder(listMenu, listPembelian):
  tryAgainPrice = 0
  
  tablelize(listMenu)
  pilihanUser = input('Masukan kode menu: ')
  validateUser = validateUserSelection(listMenu, pilihanUser.upper())
  
  while validateUser != True:
    print('Kode menu yang diinput salah / tidak valid, silahkan coba lagi !!')
    
    pilihanUser = input('Masukan kode menu: ')
    validateUser = validateUserSelection(listMenu, pilihanUser.upper())
  
  
  menuUser = selectMenu(listMenu, pilihanUser.upper())
  namaMenu = menuUser['Nama']
  
  loadingRandomate()
  randomatePrice = randomPrice()
  print(f'Menu {namaMenu} harga persatuannya menjadi {randomatePrice}')
  confirmUser = restrictedInput('Ingin coba lagi? Y/N: ', 'Input yang tersedia hanya Y/N !!', ['y','n'], str)
  
  while confirmUser == 'y':
    tryAgainPrice += 5000
    loadingRandomate()
    randomatePrice = randomPrice()
    print(f'Menu {namaMenu} harga persatuannya menjadi {randomatePrice}')
    print(f'Harga tambahan karena sudah mencoba lagi: {tryAgainPrice}')
    confirmUser = restrictedInput('Ingin coba lagi? Y/N: ', 'Input yang tersedia hanya Y/N !!', ['y','n'], str)
  
  print(f'final harga satuan untuk {namaMenu} adalah {randomatePrice}')
  
  quantityPembelian = int(input('Jumlah pembelian: '))
  
  userOrder = {}
  userOrder['Kode Menu'] = menuUser['Kode Menu']
  userOrder['Menu'] = menuUser['Nama']
  userOrder['Harga'] = randomatePrice
  userOrder['Quantity'] = quantityPembelian
  userOrder['Total harga'] = (randomatePrice + tryAgainPrice) * quantityPembelian
  userOrder['isRandom'] = True
  
  listPembelian.append(userOrder)
    
def progress_bar(t_i, c_i, bar_length, fill):
    percent = f"{100 * c_i / float(t_i):.1f}"
    percent = 100 * c_i / float(t_i)
    fill_length = bar_length * c_i // t_i
    bar = fill * fill_length + "-" * (bar_length - fill_length)

    print(f"\rRandomating: {bar} {round(percent)}%", end="")

    if c_i == t_i:
        print()

def loadingRandomate(): 
  total_iteration = 100
  for i in range(total_iteration + 1):
      progress_bar(total_iteration, i, 15, ">")
      time.sleep(0.01)

def tablelize(tableObject):
  header = tableObject[0].keys()
  rows = []
  for data in tableObject:
    rows.append(data.values())
  print(tabulate.tabulate(rows, header, tablefmt="rounded_grid"))
  
def showMenu(menu):
  makanan = []
  minuman = []
  
  for data in menu:
    if data['Type'] == 'makanan':
      makanan.append(data)
    else :
      minuman.append(data)
  
  tablelize(makanan)
  tablelize(minuman)
  
def validateUserSelection(listMenu, userSelection):
  listOfCode = []
  for menu in listMenu:
    listOfCode.append(menu['Kode Menu'])
  
  if userSelection not in listOfCode:
    return False
  else:
    return True