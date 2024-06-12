from bs4 import BeautifulSoup
import requests

class Postagem:
    def __init__(self, texto, link):
        self.texto = texto
        self.link = link

def extrair_postagens(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Encontrar as divs com os textos
    divs = soup.findAll('div', class_='feed-post-header with-post-chapeu')

    # Encontrar as divs com os links
    divs_link = soup.findAll('div', class_='feed-post-body-title gui-color-primary gui-color-hover')

    # Extrair os textos dos spans dentro das divs
    texts = [div.find('span').text for div in divs if div.find('span')]

    # Extrair os hrefs dos links dentro das divs_link, garantindo que o atributo href exista
    links = [a['href'] for div in divs_link for a in div.find_all('a', href=True)]

    return [Postagem(texto, link) for texto, link in zip(texts, links)]

def imprimir_postagens(postagens):
    for postagem in postagens:
        print(f"Texto: {postagem.texto} | Link: {postagem.link}")

# Função principal
def main():
    url = 'https://g1.globo.com'
    requisicao = requests.get(url)
    html_content = requisicao.text
    
    postagens = extrair_postagens(html_content)
    imprimir_postagens(postagens)

if __name__ == "__main__":
    main()
