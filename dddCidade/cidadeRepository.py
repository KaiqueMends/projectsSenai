from cidadeClass import cidade


class cidadeRepository:

    def __init__(self) -> None:
        self.lista_cidades: list[cidade] = []

    def adicionarCidade(self, cidade: cidade) -> None:
        self.lista_cidades.append(cidade)

    def verificaCidade(self, ddd: int) -> bool:
        for cidade in self.lista_cidades:
            if (ddd == cidade.ddd):
                return True
        return False

    def get_cidade(self, ddd: int) -> str:
        for cidade in self.lista_cidades:
            if (ddd == cidade.ddd):
                return cidade.nomeCidade

    def __str__(self) -> str:
        formatText = "{0:<10} {1:<20}\n"
        menu = formatText.format("DDD", "Cidade")

        for cidade in self.lista_cidades:
            menu += formatText.format(cidade.ddd, cidade.nomeCidade)

        return menu