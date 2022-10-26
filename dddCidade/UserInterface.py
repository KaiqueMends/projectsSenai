from cidadeRepository import cidadeRepository


class UserInterface:
    def __init__(self, cidadeRepository: cidadeRepository) -> None:
        self.cidadeRepository = cidadeRepository

    def get_user_input(self) -> int:
        result = int(input("Qual o DDD da cidade desejada? "))
        return result

    def get_ddd_by_user(self) -> str:
        ddd = self.get_user_input()

        if (self.cidadeRepository.verificaCidade(ddd) == False):
            return "DDD não encontrado na base de dados!"

        return self.cidadeRepository.get_cidade(ddd)