from modelos.anime import Anime

class AnimeDB():

    _instance = None
    _lista_de_animes : list[Anime]

    def __init__(self: "AnimeDB"):
        self._lista_de_animes = [
            Anime("Kaguya-sama wa Kokurasetai? Tensai-tachi no Renai Zunousen", "1211111"),
            Anime("Komi-san wa, Comyushou desu.", "1211121"),
            Anime("Steins;Gate", "1222111"),
            Anime("Death Note", "1222121"),
            Anime("Blue Lock", "1221121"),
            Anime("Inazuma Eleven", "1221111"),
            Anime("Haikyuu", "12212211"),
            Anime("Kuroku no Basket", "1221211"),
            Anime("Shingeki no Kyojin", "1112221"),
            Anime("Bleach", "1111211"),
            Anime("Hunter X Hunter", "1111111"),
            Anime("Naruto", "11111212"),
            Anime("Naruto Shippuden", "11111211"),
            Anime("Fullmetal Alchemist", "111212112"),
            Anime("Fullmetal Alchemist: Brotherhood", "111212111"),
            Anime("Black Clover", "1112111"),
            Anime("Chainsaw Man", "1112211"),
            Anime("Demon Slayer: Kimetsu No Yaiba", "1112212"),
            Anime("One Punch Man ",  "112111221"),
            Anime("Jojo's Bizarre Adventure ", "1121112221"),
            Anime("Saint Seiya: Knights of the Zodiac", "112111121"),
            Anime("Jujutsu Kaisen", "112111111"),
            Anime("Boku No Hero", "1121111121"),
            Anime("One Piece", "1121121"),
            Anime("Dragon Ball Series",  "11211121"),
            Anime("Digimon", "1122121"),
            Anime("Pokemon",  "11221221"),
            Anime("Dinossauro Rei", "122111"),
            Anime("Yu-Gi-Oh!", "1122112")
        ]

    @classmethod
    def instance(cls):
        if(cls._instance is None):
            cls._instance = AnimeDB()
        return cls._instance
    
    @classmethod
    def pegar_nome_por_codigo(cls, codigo : int):
        lista_de_animes = cls.instance()._lista_de_animes
        nome : str = ""

        for anime in lista_de_animes:
            if anime._codigo == codigo:
                nome = anime._nome
        
        if nome != "":
            return nome
        
        return False