"""Entenda a lógica da função de criptografia
Recebe uma string message e um inteiro key como parâmetros
Se key e message não possuírem os tipos corretos, uma exceção deve ser lançada
Se key não for um índice positivo válido de message, retorna a string message invertida
Se key for ímpar:
divide message no índice key, inverte os caracteres de cada parte, e retorna a união das partes novamente com "_" entre elas
Se key for par:
divide message no índice key, inverte a posição das partes, inverte os caracteres de cada parte, e retorna a união das partes novamente com "_" entre elas"""

import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(1, '')

    assert encrypt_message("EERRGG", 3) == "REE_GGR"
    assert encrypt_message("EERRGG", -1) ==  "GGRREE"
    assert encrypt_message("EERRGG", 4) == "GG_RREE"
