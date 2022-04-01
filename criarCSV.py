
from asyncio.windows_events import NULL
import csv
from numbers import Integral
import sys
from tkinter.tix import INTEGER
from Questao import Pergunta, Resposta

def criarCSVPerguntas(perguntas):
    # 1. cria o arquivo
    header = ["id_pergunta", "titulo", "pergunta", "resposta1", "score1","resposta2", "score2", "tags"]
    f = open('perguntas_Pt_Stackoverflow.csv', 'a', header= header,  newline='', encoding='utf-8')

    # 2. cria o objeto de gravação
    w = csv.writer(f)
    # 3. grava as linhas
    for p in perguntas:
        respostaAceita = None
        resposta2 =  Resposta("", -100,"")
        tags = []
        for r in p.respostas:
            if respostaAceita == None:
                respostaAceita = r
            else:
                if int(r.score) > resposta2.score: resposta2 = r
        if respostaAceita == None: 
            respostaAceita = Resposta("", "" ,"")
        if resposta2.resposta == "":
            resposta2 = Resposta("", "","")
            
        for t in p.tags:
            tags.append(t)
        w.writerow([str(p.id), p.titulo, p.pergunta,respostaAceita.resposta, str(respostaAceita.score), resposta2, str(resposta2.score),  tags])

   

#if __name__ == "__main__":
#   criarCSVPerguntas()
