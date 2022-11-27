from functionIqbal import deleteKey, pesan, restrictedInput, batalPesan, tablelize, showMenu
from readMenu import menus

noMeja = input('Masukan nomer meja: ')
namaPelanggan = input('Atas nama: ')

listPembelian = []
showMenu(menus)

pesan(menus, listPembelian)

print('\n')
tablelize(listPembelian)

confirmOrder = restrictedInput('Confirm Order? Y/N: ', 'Input yang tersedia hanya Y/N !!', ['y','n'], str)

while confirmOrder.lower() != 'y':
  print(f'''1. Ingin pesan lagi
2. Ingin betalkan salah satu pesanan
3. Ingin batalkan semua pesanan''')
  
  userSelectNo = restrictedInput('Masukan pilihan (1/2/3): ', 'Input yang tersedia hanya 1/2/3 !!', ['1', '2', '3'], str)
  
  if userSelectNo == '1':
    pesan(menus, listPembelian)
  elif userSelectNo == '2':
    batalPesan(listPembelian)
  elif userSelectNo == '3':
    listPembelian.clear()
  
  print(f'Jumlah array: {len(listPembelian)}')
  print(listPembelian)
  
  if len(listPembelian) == 0:
    print('Pesanan anda telah kosong')
  else:
    print('list pesanan sekarang: ')
    tablelize(listPembelian)
  
  
  
  confirmOrder = restrictedInput('Confirm Order? Y/N: ', 'Input yang tersedia hanya Y/N !!', ['y','n'], str)
  
print('DONE')