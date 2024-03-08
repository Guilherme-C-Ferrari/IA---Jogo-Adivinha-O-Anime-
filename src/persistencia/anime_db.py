from modelos.anime import Anime

class AnimeDB():

    _instance = None
    _lista_de_animes : list[Anime]

    def __init__(self: "AnimeDB"):
        self._lista_de_animes = [
            Anime("A",1)
        ]

    @classmethod
    def instance(cls):
        if(cls._instance is None):
            cls._instance = AnimeDB()
        return cls._instance
    
    @classmethod
    def pegar_nome_por_codigo(cls, codigo : int):
        lista_de_animes = cls.instance()._lista_de_animes
        nome : str

        for anime in lista_de_animes:
            if anime._codigo == codigo:
                nome = anime._nome
        
        return nome