from functionIqbal import pesan, restrictedInput, batalSatuPesanan

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

listMinuman = [
  {
    'No': '1',
    'Nama': 'Es Teh',
    'Harga': 8000
  },
  {
    'No': '2',
    'Nama': 'Es Teh Tawar',
    'Harga': 5000
  },
  {
    'No': '3',
    'Nama': 'Susu',
    'Harga': 10000
  },
]

print(listMakanan)
print(listMinuman)

noMeja = input('Masukan nomer meja: ')
namaPelanggan = input('Atas nama: ')

listPembelian = []

pesan(listMakanan, listMinuman, listPembelian)

orderLagi = restrictedInput('Ingin pesan lagi? Y/N: ', 'Input yang tersedia hanya Y/N !!', ['y','n'], str)

while orderLagi == 'Y':
  pesan(listMakanan, listMinuman, listPembelian)
  orderLagi = restrictedInput('Ingin pesan lagi? Y/N: ', 'Input yang tersedia hanya Y/N !!', ['y','n'], str)

print('\n')
print(listPembelian)

confirmOrder = restrictedInput('Confirm Order? Y/N: ', 'Input yang tersedia hanya Y/N !!', ['y','n'], str)

while confirmOrder.lower() != 'y':
  print(f'''1. Ingin pesan lagi
2. Ingin betalkan salah satu pesanan
3. Ingin batalkan semua pesanan''')
  
  userSelectNo = restrictedInput('Masukan pilihan (No): ', 'Input yang tersedia hanya 1/2/3 !!', ['1', '2', '3'], str)
  
  if userSelectNo == '1':
    pesan(listMakanan, listMinuman, listPembelian)
  elif userSelectNo == '2':
    batalSatuPesanan(listPembelian)
  elif userSelectNo == '3':
    listPembelian.clear()
  
  print('list pesanan sekarang: ')
  print(listPembelian)
  
  confirmOrder = restrictedInput('Confirm Order? Y/N: ', 'Input yang tersedia hanya Y/N !!', ['y','n'], str)
  
print('DONE')