from persistencia.anime_db import AnimeDB
from persistencia.pergunta_db import PerguntaDB

class JogoControlador:

    @classmethod
    def rodar_jogo(cls):
        menu = "0"

        msg_menu : str = """
"---------------------MENU----------------------"
Bem-vindo ao jogo advinhe o anime!
As regras são simples, basta pensar um anime e 
responder as perguntas, tentaremos advinha-lo.
Para continuar, selecione uma das 
opções abaixo:
    1 - Jogar
    2 - Sair
"""
        while menu != "2":
            print(msg_menu)
            menu : str = input()

            match menu:
                case "1":
                    cls.advinhar_anime()
                case "2":
                    cls.finalizar()
                case _:
                    print("Opção inválida. Escolha uma opção válida.")
            

    @classmethod
    def finalizar(cls):
        exit()

    @classmethod
    def advinhar_anime(cls):
        codigo : str = "1"
        cond : bool = False

        while cond == False:

            pergunta = PerguntaDB.instance().pegar_descricao_por_codigo(codigo)

            if (pergunta == False):
                anime = AnimeDB.instance().pegar_nome_por_codigo(codigo)
                print("\n")

                if (anime == False):
                    print("Esse anime não está no nosso banco de dados.")
                    break

                print(f"O seu anime é: {anime}")
                break

            print("\n")
            print(pergunta)
            print(" 1 - Sim")
            print(" 2 - Não")
            print("\n")
            resposta : str = input()

            codigo = codigo + resposta