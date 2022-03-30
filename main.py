from asyncio.windows_events import NULL
from bs4 import BeautifulSoup
import urllib.request
from Questao  import Resposta
from Questao import Pergunta
import criarCSV

_DOMINIO = 'https://pt.stackoverflow.com/'
listaDepaginas = []
listaDePerguntas = []

def getLinks(numeroDaPagina):
    paginaHtmlComListaDePerguntas = ('https://pt.stackoverflow.com/questions/tagged/python?tab=newest&page='+ str(numeroDaPagina) +'&pagesize=50')
    page = urllib.request.urlopen(paginaHtmlComListaDePerguntas)

    soup = BeautifulSoup(page, "html.parser")
    questions = soup.find("div", id = 'questions')
    itens = questions.findAll('div', attrs = {'class':'s-post-summary js-post-summary'})
    for i in itens:
        listaDepaginas.append(i.find('a').get('href'))
          

def vistarPagina(link):
    page = urllib.request.urlopen(_DOMINIO + link)
    #teste
    #page = urllib.request.urlopen('https://pt.stackoverflow.com/questions/542643/como-realizar-o-c%c3%a1lculo-de-amplitude-m%c3%b3vel-em-listas')
    id = link.split('/')[2]
    pergunta = Pergunta(NULL, NULL, NULL, NULL, NULL)
    respostas = []
    tags = []
    pergunta.id = id

    soup = BeautifulSoup(page, "html.parser")
    pergunta.titulo = soup.find('h1').text
    #print (soup.find('div', attrs = {'class':'js-vote-count flex--item d-flex fd-column ai-center fc-black-500 fs-title'}))
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
        
    listaDePerguntas.append(pergunta)
    
if __name__ == "__main__":
    numeroDaPagina = 1
    while numeroDaPagina < 181:
    
    
        getLinks(numeroDaPagina)
        numeroDaPagina = numeroDaPagina + 1
        print (numeroDaPagina)
            
    i = 1
    for pagina in listaDepaginas:
        #teste
        #if i == 10 : break
        vistarPagina(pagina)
        print(i +1)
        i = i + 1
    criarCSV.criarCSVPerguntas(listaDePerguntas)
