from functionAlfa import restrictedInput, tablelize
from functionFajar import validateUserSelection

def batalPesan(listPembelian):
  tablelize(listPembelian, 'rounded_grid')
  cancelPesanan(listPembelian)
  
  batalLagiGa = restrictedInput('Ingin batalkan pesanan lagi? Y/N: ', 'Input yang tersedia hanya Y/N', ['y', 'n'], str)
  
  while batalLagiGa == 'y':
    cancelPesanan(listPembelian)
    tablelize(listPembelian, 'rounded_grid')
    batalLagiGa = restrictedInput('Ingin batalkan pesanan lagi? Y/N: ', 'Input yang tersedia hanya Y/N', ['y', 'n'], str)
    
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
        print('Pesanan dibatalkan')
        break