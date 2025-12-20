import requests
from bs4 import BeautifulSoup

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

resposta = requests.get(url)

soup = BeautifulSoup(resposta.text, "html.parser")

links = soup.find_all("a")

print(f"Total de links encontrados: {len(links)}")