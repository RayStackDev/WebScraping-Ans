import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

resposta = requests.get(url)
soup = BeautifulSoup(resposta.text, "html.parser")

links = soup.find_all("a")

anexos = []

for link in links:
    href = link.get("href")
    texto = link.get_text(strip=True).lower()

    if not href:
        continue
    
    if href.lower().endswith(".pdf") and ("anexo i" in texto or "anexo ii" in texto):
        anexos.append(href)


url_base = "https://www.gov.br"

links_completos = []

for href in anexos:
    link_final = urljoin(url_base, href)
    links_completos.append(link_final)

print("Links Finais: ")
for l in links_completos:
    print(l)

    