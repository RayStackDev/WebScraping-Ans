# 🕷️ Web Scraping – Download de Anexos da ANS

Este projeto realiza **web scraping no site da ANS (Agência Nacional de Saúde Suplementar)** para localizar, baixar e compactar automaticamente os **Anexos I e II em formato PDF**, conforme solicitado em teste técnico.



## 🎯 Objetivo do Projeto

O objetivo deste projeto foi praticar e demonstrar:

- Web scraping com **Python**
- Consumo de páginas HTML
- Extração e filtragem de links
- Download de arquivos PDF
- Compactação de arquivos em ZIP
- Organização de projeto e uso do Git/GitHub



## ✨ O que o script faz

- Acessa o site oficial da ANS
- Analisa a estrutura HTML da página
- Localiza os links dos **Anexos I e II (PDF)**
- Exibe os links encontrados no terminal
- Cria automaticamente a pasta `anexos/`
- Baixa os arquivos PDF para essa pasta
- Compacta os PDFs em um único arquivo `anexos.zip`



## 🌐 Site utilizado

- https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos



## 💻 Tecnologias utilizadas

- Python 3.x
- `requests` – requisições HTTP
- `beautifulsoup4` – parsing e análise de HTML
- `zipfile` – compactação de arquivos
- `os` – manipulação de arquivos e diretórios

<br>

## ⚙️ Requisitos  

- Python 3.x e bibliotecas listadas no arquivo requirements.txt.

<br>

## 📦 Instalação  

- Clone o repositório, ative o ambiente virtual no Windows com venv\Scripts\activate e instale as dependências com o comando pip install -r requirements.txt.
  
<br>

## ▶️ Como usar  

- Execute o script principal com o comando python download_anexos.py. Ao final da execução, os PDFs e o arquivo ZIP estarão disponíveis na pasta anexos.
  
<br>

## 🧪 Aprendizados  

- Este projeto reforçou conceitos práticos de web scraping, análise de HTML com BeautifulSoup, download de arquivos PDF, manipulação de arquivos e diretórios, compactação de arquivos em Python e boas práticas com Git e GitHub.

<br>

## 📌 Observações  
- O script cria automaticamente a pasta anexos caso ela não exista, apenas arquivos PDF são incluídos no arquivo ZIP e o código foi desenvolvido com foco no aprendizado.
