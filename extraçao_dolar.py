import requests 
from bs4 import BeautifulSoup

link = 'https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
requisicao = requests.get(link, headers=headers)

print(requisicao) #quando o num é igual a 200 é porque deu certo ex. <Response [200]>
site = BeautifulSoup(requisicao.text, 'html.parser') 

#começando o processo de raspagem de dados
#print(site.title)  
#titulo = site.find('title') 
#print(titulo)

pesquisa = site.find_all('input')  

cotaçao_dolar = site.find('span', class_="SwHCTb")
a = (cotaçao_dolar.get_text())
print(f'1 dolar hoje vale R${a} reais')