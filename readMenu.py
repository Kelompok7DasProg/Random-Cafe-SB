import pandas as pd

sheet_id = '1aCjs5zs3iTozmDGZqlOBl2PPmd424Ie13aTFBNzTFnA'
sheet_name = 'demo_menu'
url = f'''https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'''

myFile = pd.read_csv(url)
menus = myFile.to_dict(orient='records')