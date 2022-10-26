from pytest import MonkeyPatch
from cidadeRepository import cidadeRepository
from UserInterface import UserInterface

def testGetUserInput(monkeypatch: MonkeyPatch):
    # Arrange
    AcidadeRepository = cidadeRepository()
    user_interface = UserInterface(AcidadeRepository)

    # Act
    monkeypatch.setattr("builtins.input", lambda _: "75")
    result = user_interface.get_user_input()

    # ASsert
    assert result == 75
    assert type(result) == int