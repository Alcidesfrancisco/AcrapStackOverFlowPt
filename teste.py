import csv
import time


with  open('perguntas_Pt_Stackoverflow1.csv', 'r',  newline='', encoding='utf-8') as arquivo:

    f = csv.reader(arquivo, delimiter = ",")

    for i,linha in enumerate(f):

        if 1 == 0:
            print("Cabeçalho:", linha)
        else:
            print(linha)
    print(i)
    print(enumerate(f))