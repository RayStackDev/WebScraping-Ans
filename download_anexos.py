import requests
from bs4 import BeautifulSoup

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

resposta = requests.get(url)
soup = BeautifulSoup(resposta.text, "html.parser")

links = soup.find_all("a")

for link in links[:10]:
    href = link.get("href")
    if href and href.lower().endswith:
        print(href)