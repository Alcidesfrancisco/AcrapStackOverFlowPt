import csv
from email import header
from pathlib import Path


def criarCSVPerguntas(links):
    
    
    with open('listaDeLinks.csv', 'a',  newline='', encoding='utf-8') as f:
            
        w = csv.writer(f)
        for l in links:
            w.writerow(l)

def lerCSV():
    arquivo = open('listaDeLinks.csv')

    linhas = csv.reader(arquivo)
    links = []
    for linha in linhas:
        links.append(linha); 
        print(linha)
    arquivo.close()
    return links
    
def csvExiste():
    return  Path('listaDeLinks.csv').is_file()

    


   
