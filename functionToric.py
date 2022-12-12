from functionIqbal import randomateOrder
from functionAlfa import restrictedInput, selectMenu
from functionFajar import validateUserSelection, showMenu

def pesan(listMenu, listPembelian):
  # Tampilin menu
  showMenu(listMenu)
  
  # Tanya user ingin pake fitur randomate apa engga
  print('Peringatan !!!')
  print('Menu yang sudah dipesan melalui fitur randomate tidak bisa di batalkan !!!')
  randomateOffer = restrictedInput('Ingin menggunakan fitur randomate? Y/N: ', 'Input yang tersedia hanya Y/N !!', ['y','n'], str)
  
  if randomateOffer == 'y':
    # Kalo iya, bakal panggil function randomate
    randomateOrder(listMenu, listPembelian)
  else :
    # Kalo engga, bakal panggil function pesanSekali
    pesanSekali(listMenu, listPembelian)
    
  # Tanya user ingin order lagi engga?
  orderLagi = restrictedInput('Ingin pesan lagi? Y/N: ', 'Input yang tersedia hanya Y/N !!', ['y','n'], str)

  while orderLagi == 'y':
    # Selama user menginput Y, bakal terus mengulang proses diatas
    randomateOffer = restrictedInput('Ingin menggunakan fitur randomate? Y/N: ', 'Input yang tersedia hanya Y/N !!', ['y','n'], str)
    if randomateOffer == 'y':
      randomateOrder(listMenu, listPembelian)
      print('\n')
    else :
      pesanSekali(listMenu, listPembelian)
      print('\n')
    orderLagi = restrictedInput('Ingin pesan lagi? Y/N: ', 'Input yang tersedia hanya Y/N !!', ['y','n'], str)
    
def pesanSekali(listMenu, listPembelian):  
  # User pilih menu berdasarkan kodenya
  pilihanUser = input('Masukan kode menu: ')
  
  # Validasi pilihan user, kode menu yang dimasukan harus ada di list menu
  validateUser = validateUserSelection(listMenu, pilihanUser.upper())
  
  while validateUser == False:
    # Kalo kode menunya engga ada, bakal disuruh input ulang yang benar
    print('Kode menu yang diinput salah / tidak valid, silahkan coba lagi !!')
    
    pilihanUser = input('Masukan kode menu: ')
    validateUser = validateUserSelection(listMenu, pilihanUser.upper())
  
  # User input jumlah pembelian 
  quantityPembelian = int(input('Jumlah pembelian: '))
  
  # Tampung menu yang di pilih user
  menuUser = selectMenu(listMenu, pilihanUser.upper())
  
  # Bikin varibel penampung satu order
  userOrder = {}

  # Construct data untuk membuat satu order  
  userOrder['Kode Menu'] = menuUser['Kode Menu']
  userOrder['Menu'] = menuUser['Nama']
  userOrder['Harga'] = int(menuUser['Harga'])
  userOrder['Quantity'] = quantityPembelian
  userOrder['Total harga'] = int(menuUser['Harga']) * quantityPembelian
  userOrder['isRandom'] = False
  
  listPembelian.append(userOrder)