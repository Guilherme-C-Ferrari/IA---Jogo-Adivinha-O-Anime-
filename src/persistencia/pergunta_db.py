from modelos.pergunta import Pergunta

class PerguntaDB():

    _instance = None
    _lista_de_perguntas : list[Pergunta]

    def __init__(self: "PerguntaDB"):
        self._lista_de_perguntas = [
            Pergunta("O gênero do seu anime é ação?", "1" ),
            Pergunta("O protagonista do seu anime luta usando majoritariamente armas?", "11"),
            Pergunta("Os personagens no seu anime usam de energias espirituais/vital para lutar?", "111"),
            Pergunta("Os personages do seu anime usam alguma outra forma de energia sobrenatural", "1112"),
            Pergunta("Os personagens do seu anima lutam contra demônios?", "11122"),
            Pergunta("Os personagens do seu anime lutam contra titãs que devoram humanos?", "111222"),
            Pergunta("Os personagens do seu anime utilizam de armas modernas?", "111221"),
            Pergunta("Seu protagonista tem alguma relação com um demônio?", "11121"),
            Pergunta("O mundo do seu anime possui poderes relacionados a alquimia?", "111212"),
            Pergunta("Seu anime teve um Remake?", "1112121"),
            Pergunta("Você está pensando na ver~soa mais recente do anime?", "11121211"),
            Pergunta("Seu protagonista tem cabelo branco?", "111211"),
            Pergunta("Seu protagonista usa de espadas e anti-magia?", "1112111"),
            Pergunta("Seu protagonista é ou já foi órfão?", "1111"),
            Pergunta("Seu anime se passa em um contexto de tecnologia moderna? (Celulares internet etc...),", "11111"),
            Pergunta("Seu protagonista é um ninja?", "111112"),
            Pergunta("Você esta pensando na versão mais recente do anime?", "1111121"),
            Pergunta("Seu protagonista passa por um exame de caçador?", "111111"),
            Pergunta("Seu personagem é ou já foi possuido por algum monstro/demônio?", "11112"),
            Pergunta("Seu protagonista é um Shinigami? (ceifador de almas)", "111121"),
            Pergunta("O gênero do seu anime é comédia?", "12"),
            Pergunta("O gênero do seu anime é esporte?", "122"),
            Pergunta("O esporte do seu anime é futebol?", "1221"),
            Pergunta("O esporte do seu anime é basquete?", "12212"),
            Pergunta("Seu protagonista é facilmente esquecido pelos outros?", "122121"),
            Pergunta("O esporte do seu anime é volei?", "122122" ),
            Pergunta("Seu protagonista é baixinho se comparado com outros jogadores de volei?", "1221221"),
            Pergunta("Os personagens do seu anime utilizam poderes sobrenaturais?", "12211"),
            Pergunta("Seu protagonista é um goleiro?", "122111"),
            Pergunta("Seu protagonista participa de um projeto para selecionar o melhor jogador do Japão?", "122112"),
            Pergunta("Um dos gêneros do seu anime é suspense?", "1222"),
            Pergunta("Seu anime tem temática de viagens temporais?", "12221"),
            Pergunta("Seu anime possui um caderno que é capaz de matar qualquer um?", "122212"),
            Pergunta("o protagonista do seu anime se considera um cientista louco?", "122211"),
            Pergunta("O(s) protagonista(s) do seu anime possuem algum tipo de interesse romântico?", "121"),
            Pergunta("Seu anime se passa em um contexto escolar?", "1211"),
            Pergunta("Seu anime é focado no conselho estudantil?", "12111"),
            Pergunta("Seu anime tem um(a) protagonista com dificuldade de se comunicar?", "121112"),
            Pergunta("No seu anime os protagonistas estão tentando fazer com que alguém se confesse para eles?", "121111"),
            Pergunta("O gênero do seu anime é esporte?", "122"),
            Pergunta("Suas criaturas são seres digitais?", "112212"),
            Pergunta("Suas criaturas são seres naturais do mundo?", "1122122"),
            Pergunta("Seu protagonista é ridiculamente forte em comparação aos seus adversários? ", "11211122"),
            Pergunta("O poder do seu protagonista vem de sua própria energia vital (conhecido também com stand)? ", "112111222"),
            Pergunta("Seu protagonista passa o tempo em algum tipo de escola?", "1121111"),
            Pergunta("Seu protagonista usa os poderes do cosmo?", "11211112"),
            Pergunta("Seu personagem é possuído por algum  tipo de demônio ou ser sobrenatural?", "11211111"),
            Pergunta("Seu protagonista tem poderes que é dado por outro personagem?", "112111112"),
            Pergunta("No seu anime os personagens lutam junto de criaturas sobrenaturais?", "1122"),
            Pergunta("As criaturas do seu anime tem relação com cartas mágicas?", "11221" ),
            Pergunta("As criaturas sobrenaturais do seu anime são dinossauros?", "112211"),
            Pergunta("O protagonista do seu anime luta majoritariamente no combate corpo-a-corpo?", "112" ),
            Pergunta("Seu protagonista tem algum tipo de poder sobrenatural? ", "1121"),
            Pergunta("Seu anime se passa em um contexto de tecnologia moderna? (Celulares internet etc..)", "11211"),
            Pergunta("Seu protagonista é um pirata?", "112112"),
            Pergunta("Seu protagonista é uma Criança/Adolescente?", "112111"),
            Pergunta("Existem personagens de vários outros planetas?", "1121112")
        ]

    @classmethod
    def instance(cls):
        if(cls._instance is None):
            cls._instance = PerguntaDB()
        return cls._instance
    
    @classmethod
    def pegar_descricao_por_codigo(cls, codigo : int):
        lista_de_perguntas = cls.instance()._lista_de_perguntas
        descricao : str = ""

        for pergunta in lista_de_perguntas:
            if pergunta._codigo == codigo:
                descricao = pergunta._descricao
        
        if descricao != "":
            return descricao
        
        return False