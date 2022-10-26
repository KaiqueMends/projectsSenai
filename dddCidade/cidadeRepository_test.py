from ast import Assert
from cidadeClass import cidade
from cidadeRepository import cidadeRepository

def testAdicionarCidade():
    # Arrange
    AcidadeRepository = cidadeRepository()
    city = cidade(75, "Feira de Santana")

    # Act
    AcidadeRepository.adicionarCidade(cidade(71, "Salvador"))
    AcidadeRepository.adicionarCidade(cidade(21, "Rio de janeiro"))
    AcidadeRepository.adicionarCidade(city)

    # Assert
    assert type(AcidadeRepository.lista_cidades) == list
    assert len(AcidadeRepository.lista_cidades) == 3
    assert city in AcidadeRepository.lista_cidades
    
def testVerificaCidade():
    # Arrange
    AcidadeRepository = cidadeRepository()

    # Act
    AcidadeRepository.adicionarCidade(cidade(75, "Feira de Santana"))
    resultado = AcidadeRepository.verificaCidade(75)

    # Assert
    assert len(AcidadeRepository.lista_cidades) == 1
    assert resultado == True
