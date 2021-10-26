from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import urllib #codificar as mensagens

#pegar os contatos do excel 
contatos = pd.read_excel("Enviar.xlsx")

#entrar no whats
navegador = webdriver.Edge("C:\\Users\\wesle\\OneDrive\\Área de Trabalho\\Wesley\\python\\MeusProjetos\\automaçãowhats\\WhatsApp\\msedgedriver.exe")
navegador.get("https://web.whatsapp.com/")
time.sleep(15)

#esperar entrar no whats
while len(navegador.find_elements_by_id("side")) <1:
    time.sleep(1)

#escrever a mensagens 
for i, mensagem in enumerate(contatos['Mensagem']):
    pessoas = contatos.loc[i, "Pessoa"]
    numero  = contatos.loc[i, "Número"]
    texto = urllib.parse.quote(f"olá {pessoas}! {mensagem} ")
    link = f"https://web.whatsapp.com/send/?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) <1:
        time.sleep(1)

#Enviar a mensagem
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[2]/button').click()
    time.sleep(10)