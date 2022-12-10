from functionToric import pesan
from functionPutri import batalPesan
from functionAlfa import restrictedInput, tablelize, deleteKey, invoice
from functionFajar import showMenu
from readMenu import menus

print("*" * 50)
print("-" * 50)
print(" ")
print('Halo, Selamat Datang di Random Cafe ^_^')
print('Delivering great food with new experience!')
print('')
print("-" * 50)
print("*" * 50)
print('')
print(f'''Di Random Cafe ini kamu bisa merasakan 
experience baru dengan fitur random lho!
Randomate bisa cobain fitur ini jika berkenan 
membeli makanan atau minuman dengan harga random.
Ayo cobain, keberuntungan ada di tangan mu ya!''')
print('')
print("=" * 50)
print(" ")
print("Sudah siap pesan? Yuk catat nomor meja dan nama mu!")

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
2. Ingin batalkan salah satu pesanan
3. Ingin batalkan semua pesanan''')
  
  userSelectNo = restrictedInput('Masukan pilihan (1/2/3): ', 'Input yang tersedia hanya 1/2/3 !!', ['1', '2', '3'], str)
  
  if userSelectNo == '1':
    pesan(menus, listPembelian)
  elif userSelectNo == '2':
    batalPesan(listPembelian)
  elif userSelectNo == '3':
    for pembelian in listPembelian:
      if pembelian['isRandom'] == True:
        print('Pesanan yang telah anda buat tidak bisa dibatalkan karena terdapat pesanan dari fitur randomate')
        print('Anda hanya bisa membatalkan pesanan yang anda pesan secara normal')
        break
    else :
      listPembelian.clear()
      print("Pesanan kamu sudah di batalkan. Terima kasih sudah berkunjung")
      exit()
  
  if len(listPembelian) == 0:
    print('Pesanan anda sudah kosong')
    pesananKosong = restrictedInput('Ingin pesan lagi? Y/N: ', 'Input yang tersedia hanya Y/N !!', ['y','n'], str)
    if(pesananKosong == 'y'):
      pesan(menus, listPembelian)
    else:
      print('Pesanan kamu sudah di batalkan. Terima kasih sudah berkunjung')
  else:
    print('list pesanan sekarang: ')
    tablelize(listPembelian, 'rounded_grid')

  confirmOrder = restrictedInput('Konfirmasi Order? Y/N: ', 'Input yang tersedia hanya Y/N !!', ['y','n'], str)

total = 0
for data in listPembelian:
  total += data['Total harga']

invoice_data = deleteKey(listPembelian, ['Kode Menu', 'Total harga', 'isRandom'])

invoice(namaPelanggan, noMeja, invoice_data, total)