# 4 vezes por ano
# primeira vez em 2023

# o que vou aprender:
# automatizar qualquer tarefa.
# assistir ao vivo

# aula no ar por 24 horas.
# download do material gratuito.

# não pratique com ele durante a aula

# projeto de automatização e sistemas em python

# editor de código jupyter.

# por onde eu começo?
# sempre que eu quiser criar o código.
# criar o passo a passo do que eu quero fazer.
import pyautogui
import pyperclip
import time
# passo 1: Entrar no sistema da empresa (link no drive)

# pausa de 1 segundo para cada comandos
pyautogui.pause = 1

pyautogui.press('win') # abrir o navegador
pyautogui.write('Opera GX')
time.sleep(3)
pyautogui.press('Enter')
time.sleep(3)
pyautogui.hotkey("ctrl", "t") 
# abrir nova aba no pc, ja no navegador
# pyautogui.write('link_que_eu_quero')
# não construiram uma solução pronta para caractere especial
pyperclip.copy('https://github.com/joaovianadoamaral')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('Enter')
time.sleep(5)

# passo 2: Navegar até o local do relátorio (entra na pasta exportar)
# passo 3: exporta o relatorio(fazer o download)
# passo 4: calcular os indicadores (faturamento e quantidade de produtos)
# passo 5: Enviar um e-mail para a diretoria

# python roda em qualquer sistema

# blibiotecas 
# pyautogui - usa o controle para controlar teclado, mouse e tela do computador.
# -> auxilia nossa vida

# !pip install pyautogui
# no jupyter, no meu editor de código não precisa da !

# comandos intuitivos.

# .click -> clicar em algum lugar
# .press -> pressionar uma teclado
# .write -> escrever
# .hotkey -> atalho

# write escrever um texto.
# press somente uma tecla