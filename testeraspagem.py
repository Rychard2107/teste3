from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("https://esb.tjpb.jus.br/cp-backend/sistemas/3/processos/08331331720238152001/movimentos")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

quotes = soup.find_all("span", attrs={"class":"text"})
authors = soup.find_all("small", attrs={"class":"author"})

for quote in quotes:
    print(quote.text + "")
for author in authors:
    print(author.text)


import requests

url = 'https://esb.tjpb.jus.br/cp-backend/sistemas/3/processos/08331331720238152001/movimentos'
params = {'parametro1': 'valor1', 'parametro2': 'valor2'}  # Se houver parâmetros na sua solicitação

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    # Faça o processamento dos dados conforme necessário
    print(data)
else:
    print('Erro ao fazer a solicitação:', response.status_code)
