import random
import time
from functionAlfa import restrictedInput, selectMenu
from functionFajar import validateUserSelection

def randomPrice():
  randomInt = random.randint(5000, 40000)
  
  return round(randomInt,-3)

def randomateOrder(listMenu, listPembelian):
  tryAgainPrice = 0
  pilihanUser = input('Masukan kode menu: ')
  print('\n')
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
  print('Anda bisa mencoba untuk mengundi harga lagi, tapi akan dikenakan biaya tambahan sebesar 5000 untuk setiap percobaannya')
  confirmUser = restrictedInput('Ingin coba lagi? Y/N: ', 'Input yang tersedia hanya Y/N !!', ['y','n'], str)
  print('\n')
  
  while confirmUser == 'y':
    tryAgainPrice += 5000
    loadingRandomate()
    randomatePrice = randomPrice()
    print(f'Menu {namaMenu} harga persatuannya menjadi {randomatePrice}')
    print(f'Harga tambahan karena sudah mencoba lagi: {tryAgainPrice}')
    confirmUser = restrictedInput('Ingin coba lagi? Y/N: ', 'Input yang tersedia hanya Y/N !!', ['y','n'], str)
    print('\n')
  
  print(f'Harga satuan {namaMenu} menjadi {randomatePrice}')
  
  quantityPembelian = int(input('Jumlah pembelian: '))
  
  userOrder = {}
  userOrder['Kode Menu'] = menuUser['Kode Menu']
  userOrder['Menu'] = menuUser['Nama']
  userOrder['Harga'] = randomatePrice
  userOrder['Quantity'] = quantityPembelian
  userOrder['Total harga'] = (randomatePrice * quantityPembelian) + tryAgainPrice
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
      progress_bar(total_iteration, i, 30, ">")
      time.sleep(0.01)