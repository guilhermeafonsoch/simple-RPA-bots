import rpa as r
import pyautogui as p
import pandas as pd
import os as o 

r.init()
r.url('https://rpachallengeocr.azurewebsites.net/')
janela = p.getActiveWindow()
janela.maximize()
p.sleep(2)

number_of_pages = 1
while number_of_pages <= 3:
    r.table('//*[@id="tableSandbox"]', 'temp.csv')
    dados = pd.read_csv('temp.csv')
    if number_of_pages == 1:
        dados.to_csv(r'WebTable.csv', mode = 'a', index = None, header = True)
    dados.to_csv(r'WebTable.csv', mode='a', index=None, header=False)
    r.click('//*[@id="tableSandbox_next"]')
    number_of_pages += 1
r.close()
o.remove('temp.csv')
csv_to_xlsx = pd.read_csv(r'WebTable.csv')
csv_to_xlsx.to_excel(r'WebTableExcel.xlsx')