
from asyncio.windows_events import NULL
import csv
from numbers import Integral
from pathlib import Path
import sys
from Questao import Pergunta, Resposta

def criarCSVPerguntas(pergunta):
    #verifica se o arquivo já existe
    arquivo_ja_existia = Path('perguntas_Pt_Stackoverflow1.csv').is_file()
    #cria o arquivo
    header = ["id_pergunta", "titulo", "pergunta", "resposta1", "score1","resposta2", "score2", "tags"]
    f = open('perguntas_Pt_Stackoverflow.csv', 'a',  newline='', encoding='utf-8')

    #cria o objeto de gravação
    w = csv.DictWriter(f, header)
    #grava as linhas

    respostaAceita = None
    resposta2 =  Resposta("", -100,"")
    tags = []
    for r in pergunta.respostas:
        if respostaAceita == None:
            respostaAceita = r
        else:
            if int(r.score) > int(resposta2.score): resposta2 = r
    if respostaAceita == None: 
        respostaAceita = Resposta("", "" ,"")
    if resposta2.resposta == "":
        resposta2 = Resposta("", "","")
        
    for t in pergunta.tags:
        tags.append(t)


    if not arquivo_ja_existia: w.writeheader()
    w.writerow({"id_pergunta": pergunta.id,  "titulo": pergunta.titulo, "pergunta": pergunta.pergunta,"resposta1": respostaAceita.resposta, "score1": respostaAceita.score, "resposta2": resposta2, "score2": str(resposta2.score),  "tags": tags})

   

#if __name__ == "__main__":
#   criarCSVPerguntas()
