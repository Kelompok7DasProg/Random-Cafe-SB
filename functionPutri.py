from functionAlfa import restrictedInput, tablelize
from functionFajar import validateUserSelection

def batalPesan(listPembelian):
  # Tampilin list pembelian yang udah ada
  tablelize(listPembelian, 'rounded_grid')
  
  # panggil fungsi cancelPesanan
  cancelPesanan(listPembelian)
  
  # Tanya user, mau batalin pesanan lagi engga?
  batalLagiGa = restrictedInput('Ingin batalkan pesanan lagi? Y/N: ', 'Input yang tersedia hanya Y/N', ['y', 'n'], str)
  
  while batalLagiGa == 'y':
    # kalo user input y, bakal ngulangin process diatas
    tablelize(listPembelian, 'rounded_grid')
    cancelPesanan(listPembelian)
    batalLagiGa = restrictedInput('Ingin batalkan pesanan lagi? Y/N: ', 'Input yang tersedia hanya Y/N', ['y', 'n'], str)
    
def cancelPesanan(listPembelian):
  # User input kode menu mana yang mau di hapus
  noBatal = input('Masukan kode menu yang ingin dibatalkan: ')
  
  # Validasi kode yang dimasukin user harus ada di list pembelian
  validateUser = validateUserSelection(listPembelian, noBatal.upper())
  
  while validateUser != True:
    print('Kode menu yang diinput salah / tidak valid, silahkan coba lagi !!')
    
    noBatal = input('Masukan kode menu yang ingin dibatalkan: ')
    validateUser = validateUserSelection(listPembelian, noBatal.upper())
  
  for i in range(len(listPembelian)):
    print(listPembelian[i])
    # Cek kalo kodenya sama kaya yang di masukin user
    if listPembelian[i]['Kode Menu'] == noBatal.upper():
      
      # Cek is random nya True apa engga
      if listPembelian[i]['isRandom'] == True:
        # Kalo isRandomnya True, gabisa dihapus
        print('Pesanan yang dari randomate tidak bisa dibatalkan !!!')
      else :
        # Kalo false, Bakal dihapus
        del listPembelian[i]
        print('Pesanan dibatalkan')
        break