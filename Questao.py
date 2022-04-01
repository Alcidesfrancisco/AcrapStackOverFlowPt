class Resposta:

    def __init__(self, resposta, score, aceita):
        self.resposta = resposta
        self.score = score
        self.aceita = aceita

    def __str__(self):
        return self.resposta
class Pergunta:

    def __init__(self, id, titulo, pergunta, respostas, tags):
        self.id = id
        self.titulo = titulo
        self.pergunta = pergunta
        self.respostas  = respostas
        self.tags = tags

    def __str__(self):
        return str(self.pergunta)

