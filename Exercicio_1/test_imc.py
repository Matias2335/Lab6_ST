
import pytest
from imc import calcular_imc, categorizar_imc, classificar_pessoa


def test_calcular_imc():
    assert calcular_imc(70, 2) == 17.5


@pytest.mark.parametrize(
    "imc, resultado_esperado",
    [
        (17.0, "abaixo do peso"),
        (22.0, "peso normal"),
        (27.0, "sobrepeso"),
        (32.0, "obesidade"),
    ],
    ids=[
        "abaixo-do-peso",
        "peso-normal",
        "sobrepeso",
        "obesidade",
    ],
)
def test_categorizar_imc(imc, resultado_esperado):
    assert categorizar_imc(imc) == resultado_esperado


def test_classificar_pessoa():
    assert classificar_pessoa(70, 1.75) == "peso normal"
