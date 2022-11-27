import csv

myFile = open('demo_menu.csv', 'r')
reader = csv.DictReader(myFile)
menus = list(reader)