import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(1, '')

    assert encrypt_message("EERRGG", 3) == "REE_GGR"
    assert encrypt_message("EERRGG", -1) ==  "GGRREE"
    assert encrypt_message("EERRGG", 4) == "GG_RREE"
