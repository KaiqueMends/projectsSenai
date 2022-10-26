from cidadeClass import cidade
from cidadeRepository import cidadeRepository
from UserInterface import UserInterface

cidadeRepository = cidadeRepository()
cidadeRepository.adicionarCidade(cidade(75, "Feira de Santana"))
cidadeRepository.adicionarCidade(cidade(71, "Salvador"))
cidadeRepository.adicionarCidade(cidade(11, "São Paulo"))
cidadeRepository.adicionarCidade(cidade(21, "Rio de Janeiro"))
cidadeRepository.adicionarCidade(cidade(32, "Juiz de Fora"))
cidadeRepository.adicionarCidade(cidade(27, "Vitória"))
cidadeRepository.adicionarCidade(cidade(31, "Belo Horizonte"))

print(cidadeRepository)

user_interface = UserInterface(cidadeRepository)

while True:
    result = user_interface.get_ddd_by_user()
    if (result == "DDD não encontrado na base de dados!"):
        print(result)
        break
    else:
        print(result)