class Pergunta():

    _descricao : str
    _codigo : int

    def __init__(self, descricao: str, codigo : int):
        self._descricao = descricao
        self._codigo = codigo