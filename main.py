from functionIqbal import deleteKey, pesan, restrictedInput, batalPesan, tablelize, showMenu
from readMenu import menus

company_name = 'Random Cafe, inc.'
company_address = 'Margonda Raya, No.12'
company_city = 'Depok, Indonesia'

noMeja = input('Masukan nomer meja: ')
namaPelanggan = input('Atas nama: ')

listPembelian = []
showMenu(menus)

pesan(menus, listPembelian)

print('\n')
tablelize(listPembelian, 'rounded_grid')

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
    tablelize(listPembelian, 'rounded_grid')
  
  
  
  confirmOrder = restrictedInput('Confirm Order? Y/N: ', 'Input yang tersedia hanya Y/N !!', ['y','n'], str)


total = 0
for data in listPembelian:
  total += data['Total harga']

invoice_data = deleteKey(listPembelian, ['Kode Menu', 'Total harga', 'isRandom'])

print('*' * 50)
print('\t\tINVOICE RANDOM CAFE')
print('=' * 50)
print('\t\t{}'.format(company_name))
print('\t\t{}'.format(company_address))
print('\t\t{}'.format(company_city))
# print a line between sections
print('=' * 50)
print("-" * 50)
print("Nomor Meja: " + noMeja)
print("Nama Pelanggan: "+ namaPelanggan)
print(" ")
print("Ini rincian pesanan mu ya: ")
tablelize(invoice_data, "simple")
print(" ")

print("-" * 50)
print("Total Bayar       Rp. "+ str(total))
print("-" * 50)
print(" ")
print("Terima kasih "+namaPelanggan+"!")
print("Harap tunggu. Pesanan Kamu sedang kami siapkan. ")
print("Have a great day!")
print('*' * 50)