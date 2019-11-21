# -*- coding: utf-8 -*-
import time

# Alterando a codificação utilizada.
print("[*] Alterando configuração do sistema...")
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
print("[*] Sucesso!\n")
time.sleep(1)

# Importando biblioteca para conversão
print("[*] Importando biblioteca de conversão...")
import pdftotext
print("[*] Sucesso!\n")
time.sleep(1)
 
# Carregando arquivo PDF
print("[*] Importando biblioteca de conversão...")
with open("Docker-Cheat-Sheet.pdf", "rb") as file:
    pdf = pdftotext.PDF(file)
print("[*] Sucesso!\n")
time.sleep(1)

# Salvando o texto extraido em um arquivo TXT.
print("[*] Salvando o texto extraido...")
with open('output.txt', 'w') as file:
    file.write("\n\n".join(pdf))
time.sleep(2)
print("[*] Sucesso!")
print("[*] Conversão executada com sucesso... Até a próxima!\n")
