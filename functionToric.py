from functionIqbal import randomateOrder
from functionAlfa import restrictedInput, selectMenu
from functionFajar import validateUserSelection


def pesan(listMenu, listPembelian):
  randomateOffer = restrictedInput('Ingin menggunakan fitur randomate? Y/N: ', 'Input yang tersedia hanya Y/N !!', ['y','n'], str)
  
  if randomateOffer == 'y':
    randomateOrder(listMenu, listPembelian)
  else :
    pesanSekali(listMenu, listPembelian)
    
  orderLagi = restrictedInput('Ingin pesan lagi? Y/N: ', 'Input yang tersedia hanya Y/N !!', ['y','n'], str)

  while orderLagi == 'y':
    randomateOffer = restrictedInput('Ingin menggunakan fitur randomate? Y/N: ', 'Input yang tersedia hanya Y/N !!', ['y','n'], str)
    if randomateOffer == 'y':
      randomateOrder(listMenu, listPembelian)
    else :
      pesanSekali(listMenu, listPembelian)
      
    orderLagi = restrictedInput('Ingin pesan lagi? Y/N: ', 'Input yang tersedia hanya Y/N !!', ['y','n'], str)
    
def pesanSekali(listMenu, listPembelian):
  userOrder = {}
  
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