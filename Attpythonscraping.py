import requests
from bs4 import BeautifulSoup
import pandas as pd
requests.packages.urllib3.disable_warnings()

url = 'https://books.toscrape.com/'
requisicao = requests.get(url)
requisicao.encoding = 'utf-8'

extracao = BeautifulSoup(requisicao.text, 'html.parser')

contar_livros = 0
catalogo = []

for artigo in extracao.find_all('article', class_='product_pod'):
    livro = {}
    for subtitulo in artigo.find_all('h3') :
        titulo = subtitulo.get_text().strip()
        livro['Título'] = titulo
    for price in artigo.find_all('p', class_='price_color'):
        preco = price.get_text().strip()
        livro['Preço'] = preco
    catalogo.append(livro)
for contador in extracao.find_all('h3'):
    contar_livros += 1

print('Total livros:', contar_livros)