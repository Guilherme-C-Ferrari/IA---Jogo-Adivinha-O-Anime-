from modelos.pergunta import Pergunta

class PerguntaDB():

    _instance = None
    _lista_de_perguntas : list[Pergunta]

    def __init__(self: "PerguntaDB"):
        self._lista_de_animes = [
            Pergunta("A",1)
        ]

    @classmethod
    def instance(cls):
        if(cls._instance is None):
            cls._instance = Pergunta()
        return cls._instance