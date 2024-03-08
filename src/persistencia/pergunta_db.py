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
            cls._instance = PerguntaDB()
        return cls._instance
    
    @classmethod
    def pegar_descricao_por_codigo(cls, codigo : int):
        lista_de_perguntas = cls.instance()._lista_de_perguntas
        descricao : str

        for pergunta in lista_de_perguntas:
            if pergunta._codigo == codigo:
                descricao = pergunta._descricao
        
        if descricao != "":
            return descricao
        
        return False