# Passo a passo do Projeto

import pyautogui 
import time
import pandas

pyautogui.PAUSE = 0.5

# 1. Abrir o sistema

# https://dlp.hashtagtreinamentos.com/python/intensivao/login

site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "pythonimpressionador@gmail.com"
senha = "suasenhaaqui"

# 1.1 abrir o navegar
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

# 1.2 entrar no site do sistema
pyautogui.write(site)
pyautogui.press("enter")

time.sleep(3)

# 2. Fazer o login
#Point(x=689, y=468)
pyautogui.click(x=689, y=468)
pyautogui.write(email)

pyautogui.press("tab")
pyautogui.write(senha)

pyautogui.press("tab")
pyautogui.press("enter")


# 3. Abrir/Importar a base de dados de produtos para cadastrar
tabela = pandas.read_csv("produtos.csv")

print(tabela)

# 4. Cadastrar um produto
#Point(x=767, y=317)

for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo"])
    obs = str(tabela.loc[linha, "obs"])

    pyautogui.click(x=767, y=317)
    pyautogui.write(codigo)
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)


# 5. Repetir isso tudo ate acabar a lista de produtos 