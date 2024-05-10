import pyautogui
import time
import pandas



time.sleep(5)
print (pyautogui.position())
#caminho = "c:\Users\Fabio Aguero\Desktop\Python\Hashtag Programação\Python_power_up_by_fabio\ automacao_tarefas\produtos.csv"
tabela = pandas.read_csv("produtos.csv")

print(tabela)