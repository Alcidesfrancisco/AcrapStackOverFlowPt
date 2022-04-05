from asyncio.windows_events import NULL
import time
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import urllib.request
from Questao  import Resposta
from Questao import Pergunta
import criarCSV
import adicionarAoCSV
import criarCSVListadeLinks


_DOMINIO = 'https://pt.stackoverflow.com/'
listaDepaginas = []
listaDePerguntas = []

#Método que faz o scrap na lista de pergunta e retorna os links de todas as perguntas
def getLinks(numeroDaPagina):
    paginaHtmlComListaDePerguntas = ('https://pt.stackoverflow.com/questions/tagged/python?tab=newest&page='+ str(numeroDaPagina) +'&pagesize=50')
    page = urllib.request.urlopen(paginaHtmlComListaDePerguntas)

    soup = BeautifulSoup(page, "html.parser")
    questions = soup.find("div", id = 'questions')
    itens = questions.findAll('div', attrs = {'class':'s-post-summary js-post-summary'})
    for i in itens:
        listaDepaginas.append(i.find('a').get('href'))
    
    #criarCSVListadeLinks.criarCSVPerguntas(listaDepaginas)
          
#Método que visita a página da pergunta e preenche o objeto Pergunta e Resposta do módulo Questão
#Adiciona a pergunta a uma lista ou adiciona a pergunta diretamente ao CSV
def vistarPagina(link):
    page = urllib.request.urlopen(_DOMINIO + link)
    #teste para apenas uma página
    #page = urllib.request.urlopen('https://pt.stackoverflow.com/questions/542643/como-realizar-o-c%c3%a1lculo-de-amplitude-m%c3%b3vel-em-listas')
    id = link.split('/')[2]
    pergunta = Pergunta(NULL, NULL, NULL, NULL, NULL)
    respostas = []
    tags = []
    pergunta.id = id

    #uso da biblioteca Beatifulsoup para fazer o scrap
    soup = BeautifulSoup(page, "html.parser")
    
    #Scrap da página
    pergunta.titulo = soup.find('h1').text
    pergunta.pergunta = (soup.find('div', attrs = {'class': 's-prose js-post-body'}).text)
    for tag in  soup.findAll('div', attrs = {'d-flex ps-relative fw-wrap'}):
        tags = tag.text.split(' ')
    resp = soup.find('div', attrs = {'id':'answers'})
    answer = resp.findAll('div', attrs={'class': 'answer'})

    for r in answer:
        
        resposta = r.find('div', attrs = {'class': 's-prose js-post-body'}).text
        score = r.find('div', attrs = {'class': 'js-vote-count flex--item d-flex fd-column ai-center fc-black-500 fs-title'}).text
        aceita = len(r.findAll('div', attrs = {'class': 'js-accepted-answer-indicator flex--item fc-green-500 py6 mtn8'})) > 0
        objResposta = Resposta(resposta, score, aceita)
        respostas.append(objResposta)        
    

    pergunta.respostas = respostas
    pergunta.tags = tags
    for r in pergunta.respostas:
        if r.resposta == 0 : r.reposta = ""
    
    #Adiciono a pergunta a uma lista para ser adicionar de uma vez só no csv
    listaDePerguntas.append(pergunta)

    #OU

    #Adiciono a pergunta diretamente no CSV
    adicionarAoCSV.criarCSVPerguntas(pergunta)

#Método main
if __name__ == "__main__":
    numeroDaPagina = 1
    while numeroDaPagina < 181:
    
        
        if not criarCSVListadeLinks.csvExiste(): 
            getLinks(numeroDaPagina)
            print (numeroDaPagina)
            numeroDaPagina = numeroDaPagina + 1
        else:
            listaDepaginas = criarCSVListadeLinks.lerCSV()
            print (listaDepaginas)

    i = 1
    for pagina in listaDepaginas:
        #teste
        #if i == 10 : break
        try:
            vistarPagina(pagina)
            print(i +1)
            i = i + 1
        except HTTPError as error:
            print("Dormindo")
            time.sleep(5000)
            


    #Para adicionar todas as perguntas as CSV
    #criarCSV.criarCSVPerguntas(listaDePerguntas)
