from copy import deepcopy
import tabulate

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

def deleteKey(listToDelete, listOfKeyToDelete):
  
  listCopy = deepcopy(listToDelete)
  for key in listOfKeyToDelete:
    for listDict in listCopy:
      del listDict[key]
  
  return listCopy

def invoice(nama, noMeja, invoice_data, total):
  company_name = 'Random Cafe, inc.'
  company_address = 'Margonda Raya, No.12'
  company_city = 'Depok, Indonesia'

  print('*' * 50)
  print('\t\tINVOICE RANDOM CAFE')
  print('=' * 50)
  print('\t\t{}'.format(company_name))
  print('\t\t{}'.format(company_address))
  print('\t\t{}'.format(company_city))
  # print a line between sections
  print('=' * 50)
  print("-" * 50)
  print(" ")
  print("Nomor Meja: " + noMeja)
  print("Nama Pelanggan: "+ nama)
  print(" ")
  print("-" * 50)
  print(" ")
  print("Ini rincian pesanan mu ya: ")
  tablelize(invoice_data, "simple")
  print(" ")

  print("-" * 50)
  print("Total Bayar       Rp. "+ str(total))
  print("-" * 50)
  print(" ")
  print("Terima kasih "+nama+"!")
  print("Harap tunggu. Pesanan Kamu sedang kami siapkan. ")
  print("Have a great day!")
  print('*' * 50)
  
def tablelize(tableObject, gridStyle):
  header = tableObject[0].keys()
  rows = []
  for data in tableObject:
    rows.append(data.values())
  print(tabulate.tabulate(rows, header, tablefmt=gridStyle))
  
